# -*- coding: utf-8 -*-

import pandas as pd
from pathlib import Path
from aztool_akl.schemas import *
from aztool_akl.validate.data import TypeOneValidator


class TypeTemplate:
    def __init__(self, data_filepath: (str, Path), cost_filepath: (str, Path)):
        self.data_file = Path(data_filepath)
        self.cost_file = Path(cost_filepath)
        self.working_dir = self.data_file.parent
        self.output = ""
        self.preprocessed = False
        self.data = pd.read_excel(self.data_file).sort_values(DATA_SORT).dropna(
            subset=[undercore2space(pelatis)]).reset_index(drop=True)

    def _check_next_idx(self, index, column):
        try:
            return self.data[index, column] == self.data[index + 1, column]
        except KeyError:
            return False

    def _get_cost(self, region: str, material: str, quantity: int = None):
        pass

    def _preprocess(self):
        pass

    def process(self):
        pass

    def export(self):
        self.data.to_excel(self.output, index=False)
        print(f"  -> Exported file: {self.output}\n\n\n\n")
