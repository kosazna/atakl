# -*- coding: utf-8 -*-

import pandas as pd
from aztool_akl.schemas import *
from aztool_akl.utils import *


class Validator:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def validate(self):
        _missing = self.data[tomeas].isna().sum()

        if bool(_missing):
            display_warning("Column contains missing values")
            print(f"  -> {undercore2space(tomeas)} : {_missing}\n")
