# -*- coding: utf-8 -*-

# import numpy as np
from numpy import ceil
from atakl.transform.type_two import *


class TypeThreeTransformer(TypeTwoTransformer):
    def __init__(self, data_filepath: (str, Path),
                 cost_filepath: (str, Path),
                 output_path: (str, Path) = None):
        super().__init__(data_filepath, cost_filepath)
        self.label = "Lavazza"
        self.map_name = f"{self.name} - {self.label}"
        self.output = paths.akl_home.joinpath(
            f"{self.map_name}.xlsx") if output_path is None else output_path
        self.backup = f"{self.map_name}.xlsx"

    def _preprocess(self):
        if self.to_process:
            self.data.columns = TYPE_THREE_COLUMNS[:14]
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

    def process(self):
        self._preprocess()
        if self.preprocessed:
            print("  Processing...")

            self.data[kivotia] = self.data[kivotia] + ceil(
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

            self.data[total_charge] = sum(
                [self.data[atofia_paleta_charge],
                 self.data[kivotia_charge],
                 self.data[mixanes_charge]])

            self.process_per_client(last_sort_element=poli)

            self.data[poli] = self.data[poli].replace("<NULL>", "")

            self.data.loc[
                self.data[apostoli] == idiofortosi, final_charge] = 0.00

            self.data.columns = list(map(c_2space, TYPE_THREE_COLUMNS))

            print(
                f"  -> Data Process Complete: [{self.data.shape[0]}] records\n")
