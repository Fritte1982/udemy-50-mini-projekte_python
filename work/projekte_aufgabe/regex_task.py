import os
import sys
from os import  path
import re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from own_packages import path_attributes as pa

OUTPUT_PATH = pa.OUTPUT_PATH
FIlES_PATH = path.join(pa.SOURCE_DIR, "regex_task_files")
pattern = r".*?\.\s"
pattern = r'^[A-Za-z0-9,;"\'\s\-()]+[.!?]'
list_first_sentences = []
for i in os.listdir(FIlES_PATH):
    full_path = path.join(FIlES_PATH, i)
    if path.isfile(full_path):
        with open(full_path, "r", encoding="utf-8") as file:
            content = file.readline()
            #print(content)
            first_sentences= re.findall(pattern, content)
            if first_sentences:
                list_first_sentences.append(first_sentences[0])

print(list_first_sentences)