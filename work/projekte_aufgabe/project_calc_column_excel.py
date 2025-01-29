"""Aufgabe Abschnitt 5"""
from os import path
import  pandas as pd
from own_packages import  path_attributes as pa


SOURCE_DIR= pa.SOURCE_DIR
INPUT_XLSX = path.join(SOURCE_DIR, "Input.xlsx")
OUTPUT_PATH= pa.OUTPUT_PATH
result_xlsx_out = path.join(OUTPUT_PATH, "output.xlsx")

df = pd.read_excel(INPUT_XLSX)
df["Total"] = df["Price"] * df["Quantity"]
print(df)
df.to_excel(result_xlsx_out, index=False)
print(df.info())
