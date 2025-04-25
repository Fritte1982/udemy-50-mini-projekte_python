import os
import sys
import sqlite3
from pprint import pprint
import  pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from own_packages import path_attributes as pa
from tabulate import tabulate

SOURCE_PATH = pa.SOURCE_DIR
dbfile = os.path.join(SOURCE_PATH,"data.db")

conn = sqlite3.connect(dbfile)
cursor = conn.cursor()

query = """
SELECT * FROM albums
WHERE Title LIKE '%Live%' AND LENGTH(Title) >10
"""
cursor.execute(query)
raw_data = cursor.fetchall()
describe = cursor.description
headers =  [i[0] for i in describe]
pprint(describe)
pprint(raw_data)
pprint(headers)
df = pd.DataFrame(raw_data, columns=headers)
df = df.set_index("AlbumId")
print(df)
conn.close()

tabelle = tabulate(tabular_data=raw_data,headers= headers, tablefmt="psql")
print(tabelle)