# -*- coding: utf-8 -*-

import numpy as np
from atakl.transform.template import *


class PTBLavazza(TypeTemplate):
    def __init__(self, data_filepath: Union[str, Path],
                 cost_filepath: Union[str, Path],
                 output_path: Union[str, Path] = None,
                 mode='GUI'):
        super().__init__(data_filepath, cost_filepath, mode)

        self.name = "PT Beverages"
        self.label = "Lavazza"
        self.map_name = f"{self.name} - {self.label}"
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
                if material == paleta or material == mixani:
                    if region != 'ΑΤΤΙΚΗ':
                        return round2(
                            self.costs.loc[region, material] * quantity)
                    else:
                        if quantity >= 21:
                            return round2(quantity * 9)
                        elif quantity >= 11:
                            return round2(quantity * 12)
                        elif quantity > 0:
                            return round2(quantity * 13)
                        else:
                            return 0.0
                else:
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
        self.data.loc[
            self.data[pelatis] == "ΤΡΟΦΟΔΟΣΙΑ ΙΚΕ", tomeas] = "ΜΑΚΕΔΟΝΙΑ"

        self.data[sunolika_temaxia] = self.data[sunolika_temaxia].fillna(
            0).astype(int)
        self.data[atofia_paleta] = self.data[atofia_paleta].fillna(
            0).astype(int)
        self.data[kivotia] = self.data[kivotia].fillna(0).astype(int)
        self.data[upoloipo_se_temaxia] = self.data[
            upoloipo_se_temaxia].fillna(
            0).astype(int)
        self.data[mixanes] = self.data[mixanes].fillna(0).astype(int)
        self.data[stand] = self.data[stand].fillna(0).astype(int)

        self.data[poli] = self.data[poli].fillna("<NULL>")

        self.preprocessed = True

    def process(self):
        self._preprocess()

        self.log("Processing...", Display.INFO)

        self.data[kivotia] = self.data[kivotia] + np.ceil(
            self.data[upoloipo_se_temaxia] / 6).astype(int)

        self.data[upoloipo_se_temaxia] = 0

        self.data[atofia_paleta_charge] = self.data.apply(
            lambda x: self.get_cost(x[tomeas], paleta, x[atofia_paleta]),
            axis=1)

        self.data[kivotia_charge] = self.data.apply(
            lambda x: self.get_cost(x[tomeas], kivotio, x[kivotia]),
            axis=1)

        self.data[mixanes_charge] = self.data.apply(
            lambda x: self.get_cost(x[tomeas], mixani, x[mixanes]),
            axis=1)

        self.data[kivotia_charge] = self.data.apply(
            lambda x: self._finalize_cost(x[tomeas], x[kivotia_charge]),
            axis=1)

        self.data['stand_charge'] = self.data.apply(
            lambda x: self.get_cost(x[tomeas], stand, x[stand]),
            axis=1)

        self.data[total_charge] = sum(
            [self.data[atofia_paleta_charge],
                self.data[kivotia_charge],
                self.data[mixanes_charge],
                self.data['stand_charge']])

        self.process_rows()

        self.data[poli] = self.data[poli].replace("<NULL>", "")

        self.data.loc[
            self.data[apostoli] == idiofortosi, final_charge] = 0.00

        self.process_epinaulo()
        
        self.data[kostos_metaforas] = self.data[final_charge]
        self.data[strech] = ''

        self.data = self.data[info_map[self.map_name]['akl_cols']]

        self.data.columns = info_map[self.map_name]['formal_cols']

        self.log(f"Data Process Complete: [{self.data.shape[0]}] records\n",
                 Display.INFO)

        self.to_export = True
