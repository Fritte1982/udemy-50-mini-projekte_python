import sys
import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import streamlit as st

# Gehe zwei Ordner zurück vom aktuellen Dateipfad und füge den Pfad hinzu

from xlsx_to_json_tutorial import xlx_to_json

st.title("Front XLSX to JSON")
st.write("Upload a .xlsx file to convert it to JSON")
