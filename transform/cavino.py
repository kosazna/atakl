# -*- coding: utf-8 -*-

from atakl.transform.template import *


class Cavino(TypeTemplate):
    def __init__(self, data_filepath: (str, Path),
                 cost_filepath: (str, Path),
                 output_path: (str, Path) = None,
                 mode='GUI'):
        super().__init__(data_filepath, cost_filepath, mode)

        self.name = "Cavino"
        self.map_name = f"{self.name}"
        self.backup = f"{self.map_name}.xlsx"

        self.output = paths.akl_home.joinpath(
            f"{self.map_name}.xlsx") if output_path is None else output_path

        self.costs = pd.read_excel(self.cost_file,
                                   sheet_name=self.name).set_index(
            c_2space(tomeas), drop=True)

        self.data = self.set_data(data_filepath, self.map_name)
        self.validator.set_data(self.data)

    def get_cost(self, region: str, material: str, quantity: int = None):
        if region == "ΕΞΑΓΩΓΗ":
            return 0.00
        else:
            try:
                return round2(self.costs.loc[region, material] * quantity)
            except KeyError:
                return 0.00

    def _finalize_cost(self, region: str, charge: float):
        wall = round2(self.get_cost(region, paleta, 1))
        if charge > wall:
            return wall
        return charge

    def _preprocess(self):
        if self.to_process:
            keep = info_map[self.map_name]['init']
            self.data.columns = CAVINO[:keep]
            self.data = self.data.sort_values(DATA_SORT2).reset_index(drop=True)
            self.data[sunolika_temaxia] = self.data[sunolika_temaxia].fillna(
                0).astype(int)
            self.data[atofia_paleta] = self.data[atofia_paleta].fillna(
                0).astype(int)
            self.data[kivotia] = self.data[kivotia].fillna(0).astype(int)
            self.data[upoloipo_se_temaxia] = self.data[
                upoloipo_se_temaxia].fillna(
                0).astype(int)
            self.data[mixanes] = self.data[mixanes].fillna(0).astype(int)

            self.data[poli] = self.data[poli].fillna("<NULL>")

            self.preprocessed = True
