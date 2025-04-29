"""Abschnitt 5 des Kurses """
import sys
import os
from os import path
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from own_packages import path_attributes as pa



SOURCE_XLSX= pa.SOURCE_XLSX
OUTPUT_PATH = pa.OUTPUT_PATH
print(OUTPUT_PATH)
bonus_output_xlsx = path.join(OUTPUT_PATH,"employee_bonus.xlsx")

df = pd.read_excel(SOURCE_XLSX, index_col=0)
print(df.head())

df["Bonus"] = df["Salary"] * (10/100)
print(df.head())
df.to_excel(bonus_output_xlsx)
