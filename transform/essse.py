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
        self.validator = Validator(self.data, self.map_name, mode)

    def get_cost(self, region: str, material: str, quantity: int = None):
        if region == "ΕΞΑΓΩΓΗ":
            return 0.00
        else:
            try:
                return round2(self.costs.loc[region, material] * quantity)
            except KeyError as e:
                self.log(e, Display.ERROR)
                return 0.00

    def _finalize_cost(self, region: str, charge: float):
        wall = round2(self.get_cost(region, full_pallets, 1))
        if charge > wall:
            return wall
        return charge

    def _preprocess(self):
        self.data[full_pallets] = self.data[full_pallets].fillna(
            0).astype(int)
        self.data[cartons] = self.data[cartons].fillna(0).astype(int)
        self.data[weight] = self.data[weight].fillna(0).astype(int)

        self.data[city] = self.data[city].fillna("<NULL>")

        self.preprocessed = True

    def process_rows(self, insert_into='last'):
        self.data[final_charge] = 0.0

        hold_idx = []
        hold = []
        hold_weight = []
        hold_cartons = []

        for i in self.data.itertuples():
            minimum = self.get_minimum(i.Delivery_Area)

            if self._check_idxs(i.Index, info_map[self.map_name]['check_idxs']):
                hold_idx.append(i.Index)
                hold.append(i.Συνολική_Χρέωση)
                hold_weight.append(i.Weight_in_kg)
                hold_cartons.append(i.Cartons)
            else:
                if hold:
                    hold_idx.append(i.Index)
                    hold.append(i.Συνολική_Χρέωση)
                    hold_weight.append(i.Weight_in_kg)
                    hold_cartons.append(i.Cartons)

                    whole = round2(sum(hold))
                    total_weight = sum(hold_weight)
                    total_cartons = sum(hold_cartons)

                    has_pal = (total_weight / 6) + total_cartons >= 11

                    if has_pal:
                        _max = self.get_cost(i.Delivery_Area,
                                             c_2space(full_pallets), 1)

                        if whole > _max:
                            _mul = self.data.loc[hold_idx[0], pallets]
                            _cost = _mul * _max

                            self.data.loc[i.Index, final_charge] = _cost
                        else:
                            for idx, value in zip(hold_idx, hold):
                                self.data.loc[idx, final_charge] = value
                    elif whole > minimum:
                        for idx, value in zip(hold_idx, hold):
                            self.data.loc[idx, final_charge] = value
                    else:
                        if insert_into == 'first':
                            _df_index = hold_idx[0]
                            self.data.loc[_df_index, final_charge] = minimum
                        elif insert_into == 'max':
                            _position = hold.index(max(hold))
                            _df_index = hold_idx[_position]
                            self.data.loc[_df_index, final_charge] = minimum
                        else:
                            self.data.loc[i.Index, final_charge] = minimum

                    hold_idx = []
                    hold = []
                    hold_weight = []
                    hold_cartons = []
                else:
                    if i.Συνολική_Χρέωση > minimum:
                        self.data.loc[
                            i.Index, final_charge] = i.Συνολική_Χρέωση
                    else:
                        self.data.loc[i.Index, final_charge] = minimum

    def process(self):
        auth = Authorize(self.map_name, self.log)

        if auth.user_is_licensed():
            self._preprocess()

            self.log("Processing...", Display.INFO)

            pallet_charge = self.data.apply(
                lambda x: self.get_cost(
                    x[delivery_area], c_2space(full_pallets), x[full_pallets]),
                axis=1)

            carton_charge = self.data.apply(
                lambda x: self.get_cost(
                    x[delivery_area], cartons, x[cartons]), axis=1)

            weight_charge = self.data.apply(
                lambda x: self.get_cost(
                    x[delivery_area], c_2space(weight), x[weight]), axis=1)

            self.data['pallet_charge'] = self.data.apply(
                lambda x: self.get_cost(
                    x[delivery_area], c_2space(full_pallets), x[full_pallets]),
                axis=1)

            self.data['carton_charge'] = self.data.apply(
                lambda x: self.get_cost(
                    x[delivery_area], cartons, x[cartons]), axis=1)

            self.data['weight_charge'] = self.data.apply(
                lambda x: self.get_cost(
                    x[delivery_area], c_2space(weight), x[weight]), axis=1)

            self.data[total_charge] = sum([pallet_charge,
                                           carton_charge,
                                           weight_charge])

            self.process_rows(insert_into='last')

            self.data[city] = self.data[city].replace("<NULL>", "")

            self.data.loc[
                self.data[delivery_method] == idiofortosi, final_charge] = 0.00

            self.data.loc[self.data[order_code].str.startswith(
                'PAL', na=False), final_charge] = 0.00

            self.data[delivery_cost] = self.data[final_charge]

            self.data = self.data[info_map[self.map_name]['akl_cols']]

            self.data.columns = info_map[self.map_name]['formal_cols']

            self.log(f"Data Process Complete: [{self.data.shape[0]}] records\n",
                     Display.INFO)

            self.to_export = True
        else:
            self.log("Can't process data. Contact Support", Display.INFO)
