# -*- coding: utf-8 -*-

import pandas as pd
from atakl.utilities import *


class Validator:
    def __init__(self, data: pd.DataFrame = None, mode=None):
        self.data = data
        self.log = Display(mode)
        self.map_name = None
        self.validator_map = info_map

    def columns(self, transformer: str):
        if self.data is not None:
            length = self.data.shape[1] == self.validator_map[transformer][
                "init_ncols"]
            names = all(
                [x in self.validator_map[transformer]["formal_cols"] for x in
                 self.data.columns.tolist()])
            init_length = self.validator_map[transformer]["init_ncols"]
            init_names = self.validator_map[transformer]["formal_cols"]
            tip = False

            if length and names:
                self.log("Data structure validation: OK\n", Display.INFO)
            elif not length and not names:
                self.log("Data structure validation: FAILED", Display.ERROR)
                self.log(f'  Correct number of columns: {init_length}')
                self.log(f'  Provided number of columns: {self.data.shape[1]}')
                self.log(f'  Correct names for columns:')
                for i in init_names:
                    self.log(i)
                tip = True
            elif length and not names:
                self.log("Data structure validation: FAILED", Display.ERROR)
                self.log(f'  Correct names for columns:')
                for i in init_names:
                    self.log(i)
                tip = True
            else:
                self.log("Data structure validation: FAILED", Display.ERROR)
                self.log(f'  Correct number of columns: {init_length}')
                self.log(f'  Provided number of columns: {self.data.shape[1]}')
                tip = True

            if tip:
                self.log("Verify you select the correct process for the files",
                         Display.INFO)
                return False
            return True
        else:
            self.log("Validator data are not set", Display.ERROR)
            return False

    def missing(self):
        if self.data is not None:
            has_missing = False
            bools = []
            for i in self.validator_map[self.map_name]['sort']:
                _missing = self.data[i].isna().sum()
                bools.append(bool(_missing))

                if _missing:
                    has_missing = True
                    self.log(f"Missing values - {c_2space(i)} : {_missing}")

            if has_missing:
                self.log("Missing values may lead to wrong calculations\n",
                         Display.WARNING)

            return any(bools)
        else:
            self.log("Validator data are not set", Display.ERROR)

    def set_data(self, data: pd.DataFrame):
        self.data = data

    def set_process_name(self, name):
        self.map_name = name
