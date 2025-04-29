import pandas as pd

in_xlsx_path:str = (
    r"C:\Users\richa\git-projekte\udemy-50-mini-projekte_python\files_data\Input.xlsx"
    )

output_xls = (
    r"C:\Users\richa\git-projekte\udemy-50-mini-projekte_python\output" +
    r"\output.xlsx")


df = pd.read_excel(in_xlsx_path)

df["Total"] = df["Price"] * df["Quantity"]
print(df) 

df.to_excel(output_xls, index=False)