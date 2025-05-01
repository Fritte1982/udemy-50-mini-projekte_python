import sys
import os
# Gehe zwei Ordner zurück vom aktuellen Dateipfad und füge den Pfad hinzu
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from pathlib import Path
from own_packages import path_attributes as pa
import pandas as pd
from pprint import pprint

xlsx_dir = Path(pa.SOURCE_DIR) / "web_app_streamlit_sources"
xlsx_in_path = xlsx_dir / "europe (2).xlsx"
json_out_path = Path(pa.OUTPUT_PATH) / "europe_2.json"

def xlsx_to_json(xlsx_in):
    df = pd.read_excel(xlsx_in)
    json_data = df.to_json(orient="records")
    return json_data

def xlsx_to_csv(xlsx_in):
    df = pd.read_excel(xlsx_in)
    csv_data = df.to_csv(index=False)
    return csv_data


def main():
    pprint(xlsx_to_json(xlsx_in_path))

if __name__ == '__main__':
    main()

