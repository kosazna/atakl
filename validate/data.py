# -*- coding: utf-8 -*-

import pandas as pd
from atakl.utilities.schemas import *
from atakl.utilities.utils import *


class Validator:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.validator_map = {
            "Concepts": {"init": 12,
                         "names": list(map(c_2space, TYPE_ONE_COLUMNS))},
            "PT Beverages - Spirits": {"init": 17,
                                       "names": list(
                                           map(c_2space, TYPE_TWO_COLUMNS))},
            "PT Beverages - Lavazza": {"init": 14,
                                       "names": list(
                                           map(c_2space, TYPE_THREE_COLUMNS))}
        }

    def columns(self, transformer: str):
        length = self.data.shape[1] == self.validator_map[transformer]["init"]
        names = all([x in self.validator_map[transformer]["names"] for x in
                     self.data.columns.tolist()])
        init_length = self.validator_map[transformer]["init"]
        init_names = self.validator_map[transformer]["names"]
        tip = False

        if length and names:
            display("Data structure validation: OK")
        elif not length and not names:
            display_error("Data structure validation: FAILED")
            print(f'  Correct number of columns: {init_length}')
            print(f'  Provided number of columns: {self.data.shape[1]}\n')
            print(f'  Correct names for columns:')
            for i in init_names:
                print(i)
            tip = True
        elif length and not names:
            display_error("Data structure validation: FAILED")
            print(f'  Correct names for columns:')
            for i in init_names:
                print(i)
            tip = True
        else:
            display_error("Data structure validation: FAILED")
            print(f'  Correct number of columns: {init_length}')
            print(f'  Provided number of columns: {self.data.shape[1]}\n')
            tip = True

        if tip:
            display("Verify you selected the correct process for the files")
            return False
        return True

    def missing(self):
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
            display_warning("There are columns with missing values:")

            if bool(imerominia_missing):
                print(f"  -> {c_2space(imerominia)} : {imerominia_missing}")
            if bool(pelatis_missing):
                print(f"  -> {c_2space(pelatis)} : {pelatis_missing}")
            if bool(tomeas_missing):
                print(f"  -> {c_2space(tomeas)} : {tomeas_missing}")
            if bool(paradosi_missing):
                print(f"  -> {c_2space(paradosi)} : {paradosi_missing}")
            if bool(poli_missing):
                print(f"  -> {c_2space(poli)} : {poli_missing}")

            display_warning("Missing values may lead to wrong calculations")

        return any(bool_missing)
