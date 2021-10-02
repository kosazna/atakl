# -*- coding: utf-8 -*-

from atakl.transform.template import *


class Kitsanelis(TypeTemplate):
    def __init__(self,
                 data_filepath: Union[str, Path],
                 cost_filepath: Union[str, Path],
                 output_path: Union[str, Path] = None,
                 mode='GUI'):
        super().__init__(data_filepath, cost_filepath, mode)

        self.name = "Kitsanelis"
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
        wall = round2(self.get_cost(region, paleta, 1))
        if charge > wall:
            return wall
        return charge

    def _preprocess(self):
        self.data[kivotia_diafimistikou] = self.data[kivotia_diafimistikou].fillna(
            0).astype(int)
        self.data[kivotia_ximou] = self.data[kivotia_ximou].fillna(
            0).astype(int)
        self.data[kivotia_6fialon] = self.data[kivotia_6fialon].fillna(
            0).astype(int)
        self.data[kivotia_12fialon] = self.data[kivotia_12fialon].fillna(
            0).astype(int)

        self.data[poli_paradosis] = self.data[poli_paradosis].fillna("<NULL>")

        self.preprocessed = True

    def process(self):
        auth = Authorize(self.map_name, self.log)

        if auth.user_is_licensed():
            self._preprocess()

            self.log("Processing...", Display.INFO)

            self.data[diafimistiko_dist_charge] = self.data.apply(
                lambda x: self.get_cost(
                    x[tomeas], diafimistiko, x[kivotia_diafimistikou]),
                axis=1)

            self.data[ximoi_dist_charge] = self.data.apply(
                lambda x: self.get_cost(x[tomeas], ximoi, x[kivotia_ximou]),
                axis=1)

            self.data[fiales6_dist_charge] = self.data.apply(
                lambda x: self.get_cost(x[tomeas], fiales6, x[kivotia_6fialon]),
                axis=1)

            self.data[fiales12_dist_charge] = self.data.apply(
                lambda x: self.get_cost(
                    x[tomeas], fiales12, x[kivotia_12fialon]),
                axis=1)

            self.data[total_charge] = sum([self.data[diafimistiko_dist_charge],
                                           self.data[ximoi_dist_charge],
                                           self.data[fiales6_dist_charge],
                                           self.data[fiales12_dist_charge]])

            self.process_rows(insert_into='max')

            self.data.loc[
                self.data[apostoli] == idiofortosi, final_charge] = 0.00

            self.data[final_dist_charge] = self.data[final_charge]

            self.data = self.data[info_map[self.map_name]['akl_cols']]

            self.data.columns = info_map[self.map_name]['formal_cols']

            self.log(f"Data Process Complete: [{self.data.shape[0]}] records\n",
                     Display.INFO)

            self.to_export = True
        else:
            self.log("Can't process data. Contact Support", Display.INFO)
