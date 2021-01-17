# -*- coding: utf-8 -*-

from atakl.transform.template import *


class Giochi(TypeTemplate):
    def __init__(self, data_filepath: Union[str, Path],
                 cost_filepath: Union[str, Path],
                 output_path: Union[str, Path] = None,
                 mode='GUI'):
        super().__init__(data_filepath, cost_filepath, mode)

        self.name = "Giochi"
        self.map_name = f"{self.name}"
        self.backup = f"{self.map_name}.xlsx"

        self.output = paths.akl_home.joinpath(
            f"{self.map_name}.xlsx") if output_path is None else output_path

        self.costs = pd.read_excel(self.cost_file,
                                   sheet_name=self.name).set_index(
            c_2space(tomeas), drop=True)

        self.data = self.set_data(data_filepath, self.map_name)
        self.validator.set_data(self.data)

    def get_cost(self,
                 client: str,
                 region: str,
                 material: str,
                 quantity: int = None):
        if region == "ΕΞΑΓΩΓΗ":
            return 0.00
        else:
            try:
                if client == 'JUMBO Α.Ε.Ε' and region == 'ΣΤ.ΕΛΛΑΔΑ - ΕΥΒΟΙΑ':
                    return round2(self.costs.loc['ΑΤΤΙΚΗ', material] * quantity)
                return round2(self.costs.loc[region, material] * quantity)
            except KeyError as e:
                self.log(e, Display.ERROR)
                return 0.00

    def _finalize_cost(self, client: str, region: str, charge: float):
        wall = round2(self.get_cost(client, region, paleta, 1))
        if charge > wall:
            return wall
        return charge

    def _preprocess(self):
        if self.to_process:
            keep = info_map[self.map_name]['init_ncols']
            self.data.columns = info_map[self.map_name]['akl_cols'][:keep]
            sort_rule = info_map[self.map_name]['sort']
            self.data = self.data.sort_values(sort_rule).reset_index(drop=True)

            self.data[paletes] = self.data[paletes].fillna(0).astype(int)
            self.data[ogkos] = self.data[ogkos].fillna(0.0).astype(float)

            self.data[paradosi] = self.data[paradosi].fillna("<NULL>")

            self.preprocessed = True

    def process_volume(self, insert_into='last'):
        loc_attiki = self.data[tomeas] == 'ΑΤΤΙΚΗ'
        attiki = self.data.loc[loc_attiki]

        attiki[final_charge] = 0.0

        hold_idx = []
        hold_volume = []
        hold_charge = []

        minimum_volume = 0.4
        minimum_charge = self.get_minimum('ΑΤΤΙΚΗ')

        for i in attiki.itertuples():
            if self._check_idxs(i.Index, info_map[self.map_name]['check_idxs']):
                hold_idx.append(i.Index)
                hold_volume.append(i.Όγκος)
                hold_charge.append(i.Συνολική_Χρέωση)
            else:
                if hold_charge:
                    hold_idx.append(i.Index)
                    hold_volume.append(i.Όγκος)
                    hold_charge.append(i.Συνολική_Χρέωση)

                    whole_volume = round2(sum(hold_volume))

                    if whole_volume > minimum_volume:
                        for idx, value in zip(hold_idx, hold_charge):
                            self.data.loc[idx, final_charge] = value
                    else:
                        if insert_into == 'last':
                            self.data.loc[
                                i.Index, final_charge] = minimum_charge
                        else:
                            _position = hold_charge.index(max(hold_charge))
                            _df_index = hold_idx[_position]
                            self.data.loc[
                                _df_index, final_charge] = minimum_charge

                    hold_idx = []
                    hold_charge = []
                    hold_volume = []
                else:
                    if i.Όγκος > minimum_volume:
                        self.data.loc[
                            i.Index, final_charge] = i.Συνολική_Χρέωση
                    else:
                        self.data.loc[i.Index, final_charge] = minimum_charge

    def process(self):
        self._preprocess()
        if self.preprocessed:
            self.log("Processing...", Display.INFO)

            self.data[paletes_dist_charge] = self.data.apply(
                lambda x: self.get_cost(x[pelatis], x[tomeas], paleta,
                                        x[paletes]), axis=1)

            self.data[kivotia_lampades_dist_charge] = ''
            self.data[kivotia_paixnidia_dist_charge] = ''

            self.data[ogkos_dist_charge] = self.data.apply(
                lambda x: self.get_cost(x[pelatis], x[tomeas], kuviko,
                                        x[ogkos]), axis=1).round(2)

            self.data[total_charge] = sum([self.data[paletes_dist_charge],
                                           self.data[ogkos_dist_charge]])

            self.process_rows()
            self.process_volume()

            self.data[paradosi] = self.data[paradosi].replace("<NULL>", "")

            self.data.loc[
                self.data[apostoli] == idiofortosi, final_charge] = 0.00

            self.data[final_dist_charge] = self.data[final_charge]

            self.data = self.data[info_map[self.map_name]['akl_cols']]

            self.data.columns = info_map[self.map_name]['formal_cols']

            self.log(f"Data Process Complete: [{self.data.shape[0]}] records\n",
                     Display.INFO)

            self.to_export = True
        else:
            self.log("Process did not execute due to errors.", Display.INFO)
