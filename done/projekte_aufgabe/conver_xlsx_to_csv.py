import pandas as pd

PATH_XLSX_IN:str = r"C:\Users\richa\git-projekte\udemy-50-mini-projekte_python\files_data\europe_1.xlsx"
OUTPUT_PATH:str = r"C:\Users\richa\git-projekte\udemy-50-mini-projekte_python\output"
csv_out: str = OUTPUT_PATH + r"\europa.csv"

df = pd.read_excel(PATH_XLSX_IN)
df.to_csv(csv_out, index=False)
