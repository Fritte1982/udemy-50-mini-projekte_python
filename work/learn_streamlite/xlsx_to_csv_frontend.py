from xlsx_converts import xlsx_to_csv
import streamlit as st



st.title("Front XLSX to CSV")
st.write("Upload a .xlsx file to convert it to CSV")
uploaded_file = st.file_uploader("Upload a .xlsx file", type=["xlsx","xls"])
if uploaded_file is not None:
    generated_csv = xlsx_to_csv(uploaded_file)
    st.write(generated_csv)
    st.download_button("Download CSV",file_name="convert.csv",data=generated_csv,mime="text/csv")