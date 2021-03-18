# -*- coding: utf-8 -*-

from atakl.transform.template import *


class Essse(TypeTemplate):
    def __init__(self, data_filepath: Union[str, Path],
                 cost_filepath: Union[str, Path],
                 output_path: Union[str, Path] = None,
                 mode='GUI'):
        super().__init__(data_filepath, cost_filepath, mode)

        self.name = "Essse"
        self.map_name = f"{self.name}"
        self.backup = f"{self.map_name}.xlsx"

        self.output = paths.akl_home.joinpath(
            f"{self.map_name}.xlsx") if output_path is None else output_path

        self.costs = pd.read_excel(self.cost_file,
                                   sheet_name=self.name).set_index(
            c_2space(tomeas), drop=True)

        self.data = self.set_data(data_filepath, self.map_name)
        self.validator.set_process_name(self.map_name)
        self.validator.set_data(self.data)

    def get_cost(self, region: str, material: str, quantity: int = None):
        if region == "ΕΞΑΓΩΓΗ":
            return 0.00
        else:
            try:
                return round2(self.costs.loc[region, material] * quantity)
            except KeyError as e:
                self.log(e, Display.ERROR)
                return 0.00

    def _preprocess(self):
        if self.to_process:
            keep = info_map[self.map_name]['init_ncols']
            self.data.columns = info_map[self.map_name]['akl_cols'][:keep]
            sort_rule = info_map[self.map_name]['sort']
            self.data = self.data.sort_values(sort_rule).reset_index(drop=True)

            self.data[full_pallets] = self.data[full_pallets].fillna(
                0).astype(int)
            self.data[cartons] = self.data[cartons].fillna(0).astype(int)
            self.data[weight] = self.data[weight].fillna(0).astype(int)

            if any(self.data[pieces] != 0):
                self.log(f"{kola} column contains non-zero value.",
                         Display.WARNING)

            self.data[city] = self.data[city].fillna("<NULL>")

            self.preprocessed = True

    def process_rows(self, insert_into='last'):
        self.data[final_charge] = 0.0

        hold_idx = []
        hold = []

        for i in self.data.itertuples():
            minimum = self.get_minimum(i.Γεωγραφικός_Τομέας)

            if self._check_idxs(i.Index, info_map[self.map_name]['check_idxs']):
                hold_idx.append(i.Index)
                hold.append(i.Συνολική_Χρέωση)
            else:
                if hold:
                    hold_idx.append(i.Index)
                    hold.append(i.Συνολική_Χρέωση)

                    whole = round2(sum(hold))

                    if whole > minimum:
                        for idx, value in zip(hold_idx, hold):
                            self.data.loc[idx, final_charge] = value
                    else:
                        if insert_into == 'last':
                            self.data.loc[i.Index, final_charge] = minimum
                        else:
                            _position = hold.index(max(hold))
                            _df_index = hold_idx[_position]
                            self.data.loc[_df_index, final_charge] = minimum

                    hold_idx = []
                    hold = []
                else:
                    if i.Συνολική_Χρέωση > minimum:
                        self.data.loc[
                            i.Index, final_charge] = i.Συνολική_Χρέωση
                    else:
                        self.data.loc[i.Index, final_charge] = minimum

    def process(self):
        self._preprocess()
        if self.preprocessed:
            self.log("Processing...", Display.INFO)

            pallet_charge = self.data.apply(
                lambda x: self.get_cost(
                    x[delivery_area], full_pallets, x[full_pallets]), axis=1)

            carton_charge = self.data.apply(
                lambda x: self.get_cost(
                    x[delivery_area], cartons, x[cartons]), axis=1)

            weight_charge = self.data.apply(
                lambda x: self.get_cost(
                    x[delivery_area], weight, x[weight]), axis=1)

            self.data[total_charge] = sum(pallet_charge,
                                          carton_charge,
                                          weight_charge)

            self.process_rows(insert_into='max')

            self.data = self.data.set_index('index')

            self.data = pd.concat([self.data, _temp1]).sort_index()

            self.data[paradosi] = self.data[paradosi].replace("<NULL>", "")

            order = self.data[kodikos_paraggelias].str.split('-').str[
                :3].str.join('-')
            og_order = self.data[kodikos_arxikis_paraggelias].str.split(
                '-').str[:3].str.join('-')

            order_idxs = order.loc[order.isin(og_order)].index
            og_order_idxs = og_order.loc[og_order.isin(order)].index

            _charge = self.data.loc[order_idxs, final_charge].values

            _multiplier = self.data.loc[og_order_idxs, temaxia].values

            to_replace = _charge * _multiplier

            self.data.loc[order_idxs, final_charge] = to_replace

            self.data.loc[
                self.data[apostoli] == idiofortosi, final_charge] = 0.00

            self.data[kola_dist_charge] = self.data[final_charge]
            self.data[strech] = ""

            self.data = self.data[info_map[self.map_name]['akl_cols']]

            self.data.columns = info_map[self.map_name]['formal_cols']

            self.log(f"Data Process Complete: [{self.data.shape[0]}] records\n",
                     Display.INFO)

            self.to_export = True
        else:
            self.log("Process did not execute due to errors.", Display.INFO)