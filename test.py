import openpyxl
import pandas as pd


f = "D:/.temp/.dev/akl/Region_Costs_old.xlsx"
fe = pd.ExcelFile(f)

# wb = openpyxl.load_workbook(f)
# print(wb.sheetnames)

df = pd.read_excel(f, sheet_name=None)
print(df['Siganos'])

# print(fe.sheet_names)