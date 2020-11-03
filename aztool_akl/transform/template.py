# -*- coding: utf-8 -*-

import pandas as pd
from pathlib import Path
from aztool_akl.schemas import *
from aztool_akl.validate.data import Validator


class TypeTemplate:
    def __init__(self, data_filepath: (str, Path), cost_filepath: (str, Path)):
        self.data_file = Path(data_filepath)
        self.cost_file = Path(cost_filepath)
        self.working_dir = self.data_file.parent
        self.output = ""
        self.preprocessed = False
        self.data = pd.read_excel(self.data_file).dropna(
            subset=[undercore2space(pelatis)])
        self.costs = pd.DataFrame()
        self.validator = Validator(self.data)

    def _preprocess(self):
        pass

    def get_cost(self, region: str, material: str, quantity: int = None):
        pass

    def process(self):
        pass

    def _check_next_idx(self, index, column):
        try:
            return self.data.loc[index, column] == self.data.loc[
                index + 1, column]
        except KeyError:
            return False

    def get_minimum(self, region: str):
        try:
            if region == "ΕΞΑΓΩΓΗ":
                return 0.00
            else:
                return round2(self.costs.loc[region, elaxisti])
        except KeyError:
            return 0.00

    def process_per_client(self):
        self.data[final_charge] = 0.0

        hold_idx = []
        hold = []

        for i in self.data.itertuples():
            same_name = self._check_next_idx(i.Index, pelatis)

            same_date = self._check_next_idx(i.Index, imerominia)

            same_region = self._check_next_idx(i.Index, tomeas)

            same_delivery = self._check_next_idx(i.Index, paradosi)

            minimum = self.get_minimum(i.Γεωγραφικός_Τομέας)

            if all([same_name, same_date, same_region, same_delivery]):
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
                        self.data.loc[i.Index, final_charge] = minimum

                    hold_idx = []
                    hold = []
                else:
                    if i.Συνολική_Χρέωση > minimum:
                        self.data.loc[
                            i.Index, final_charge] = i.Συνολική_Χρέωση
                    else:
                        self.data.loc[i.Index, final_charge] = minimum

    def export(self):
        self.data.to_excel(self.output, index=False)
        print(f"  -> Exported file: {self.output}\n\n\n\n")
