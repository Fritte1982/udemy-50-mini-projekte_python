import pandas as pd
from pathlib import Path
from own_packages import path_attributes

PATH_XLSX_IN = Path(path_attributes.SOURCE_DIR) / "europe_1.xlsx"
OUTPUT_PATH = Path(path_attributes.OUTPUT_PATH)
csv_out = OUTPUT_PATH / "europa.csv"

df = pd.read_excel(PATH_XLSX_IN)
df.to_csv(csv_out, index=False)
