from pathlib import Path
import pandas as pd

split_char = '@'
text = "C:\\Users\\aznavouridis.k\\Desktop\\AKL_Auto\\DB_Data\\PT Beverages - Lavazza.xlsx"


splitted = text.split(split_char)
filepath = Path(splitted[0])
# print(filepath)
# sheet_name = splitted[1]


print(pd.read_excel(filepath, sheet_name=0).shape)
