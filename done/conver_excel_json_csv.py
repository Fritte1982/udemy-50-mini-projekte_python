import  pandas as pd
import json
from own_packages import path_attributes
from pathlib import Path

PATH_XLSX_IN = Path(path_attributes.SOURCE_DIR) / r"europe_1.xlsx"
OUTPUT_PATH = Path(path_attributes.OUTPUT_PATH)
json_out = OUTPUT_PATH / "europe.json"

df = pd.read_excel(PATH_XLSX_IN)
df.to_json(json_out, orient="records", indent=4)

