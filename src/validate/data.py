import pandas as pd


class TypeOneValidator:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def validate(self):
        _missing = self.data['Γεωγραφικός_Τομέας'].isna().sum()

        if bool(_missing):
            print("[WARNING] - Column contains missing values.")
            print(f"    'Γεωγραφικός Τομέας' : {_missing}\n")
