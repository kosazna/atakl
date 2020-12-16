from pathlib import Path
import pandas as pd

split_char = '@'
text = Path("C:\\Users\\aznavouridis.k\\Desktop\\AKL_Auto\\DB_Data\\PT Beverages - Lavazza.xlsx@test")


splitted = str(text).split(split_char)
filepath = Path(splitted[0])
# print(filepath)
# sheet_name = splitted[1]


print(text)
