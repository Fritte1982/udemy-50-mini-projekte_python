import os
import sys
import re
from os import  path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from own_packages import path_attributes as pa

OUTPUT_PATH = pa.OUTPUT_PATH
DOCUMENTS_PATH = path.join(pa.SOURCE_DIR, "Documents")
pattern = r"\b[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,}\b"
result_file_path =path.join( OUTPUT_PATH,"erg_mail.txt")
all_emails = []
for i in os.listdir(DOCUMENTS_PATH):
    full_path_txt = path.join(DOCUMENTS_PATH, i)
    if path.isfile(full_path_txt):
        with open (full_path_txt, "r") as file:
            content = file.read()
        emails = re.findall(pattern,content)
        for j in emails:
            all_emails.append(j)
with open(result_file_path, "w", encoding="utf-8") as file:
    for i in all_emails:
        file.write(i)
        file.write("\n")
