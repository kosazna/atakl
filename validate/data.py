# -*- coding: utf-8 -*-

import pandas as pd
from atakl.utilities import *


class Validator:
    def __init__(self, data: pd.DataFrame = None, mode=None):
        self.data = data
        self.log = Display(mode)
        self.validator_map = info_map

    def columns(self, transformer: str):
        if self.data is not None:
            length = self.data.shape[1] == self.validator_map[transformer][
                "init"]
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
            imerominia_missing = self.data[imerominia].isna().sum()
            pelatis_missing = self.data[c_2space(pelatis)].isna().sum()
            tomeas_missing = self.data[c_2space(tomeas)].isna().sum()

            try:
                paradosi_missing = self.data[c_2space(paradosi)].isna().sum()
            except KeyError:
                paradosi_missing = 0

            try:
                poli_missing = self.data[poli].isna().sum()
            except KeyError:
                poli_missing = 0

            bool_missing = [bool(imerominia_missing),
                            bool(pelatis_missing),
                            bool(tomeas_missing),
                            bool(paradosi_missing),
                            bool(poli_missing)]

            if any(bool_missing):
                self.log("There are columns with missing values:",
                         Display.WARNING)

                if bool(imerominia_missing):
                    pad = ' ' * 10
                    self.log(
                        f"{pad}- {c_2space(imerominia)} : {imerominia_missing}")
                if bool(pelatis_missing):
                    pad = ' ' * 10
                    self.log(f"{pad}- {c_2space(pelatis)} : {pelatis_missing}")
                if bool(tomeas_missing):
                    pad = ' ' * 10
                    self.log(f"{pad}- {c_2space(tomeas)} : {tomeas_missing}")
                if bool(paradosi_missing):
                    pad = ' ' * 10
                    self.log(
                        f"{pad}- {c_2space(paradosi):} : {paradosi_missing}")
                if bool(poli_missing):
                    pad = ' ' * 10
                    self.log(f"{pad}- {c_2space(poli)} : {poli_missing}")

                self.log("Missing values may lead to wrong calculations\n",
                         Display.WARNING)

            return any(bool_missing)
        else:
            self.log("Validator data are not set", Display.ERROR)

    def set_data(self, data: pd.DataFrame):
        self.data = data
