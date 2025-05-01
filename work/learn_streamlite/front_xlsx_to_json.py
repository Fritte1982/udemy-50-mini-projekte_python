"""Frontend das eine Excel-Datei in eine json wandelt und zum Download bereitstellt """
import streamlit as st
from xlsx_converts import xlsx_to_json

st.title("Front XLSX to JSON")
st.write("Upload a .xlsx file to convert it to JSON")
uploaded_file = st.file_uploader("Upload a .xlsx file", type=["xlsx","xls"])
if uploaded_file is not None:
    generated_json = xlsx_to_json(uploaded_file)
    st.json(generated_json)
    st.download_button(label="Download JSON",file_name="converted.json",
                       data=generated_json, mime="application/json")
