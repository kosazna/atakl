import pandas as pd
from aztool_akl.schemas import *


class TypeOneValidator:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def validate(self):
        _missing = self.data[tomeas].isna().sum()

        if bool(_missing):
            display_warning("Column contains missing values")
            print(f"  -> {undercore2space(tomeas)} : {_missing}\n")
