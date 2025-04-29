import  pandas as pd
import json

PATH_XLSX_IN:str = r"C:\Users\richa\git-projekte\udemy-50-mini-projekte_python\files_data\europe_1.xlsx"
OUTPUT_PATH:str = r"C:\Users\richa\git-projekte\udemy-50-mini-projekte_python\output"
json_out = OUTPUT_PATH + r"\europe.json"

df = pd.read_excel(PATH_XLSX_IN)
df.to_json(json_out, orient="records", indent=4)

