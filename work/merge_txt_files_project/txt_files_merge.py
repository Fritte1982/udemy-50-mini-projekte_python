import glob
from pathlib import Path
from own_packages import path_attributes as pa
from pprint import pprint

txt_sources_dir = Path(pa.SOURCE_DIR) / "txt_files"
txt_path_pattern = str(txt_sources_dir) + "/*.txt"
txt_out = Path(pa.OUTPUT_PATH) / "merge.txt"

txt_list =[]
for txt_file in glob.glob(txt_path_pattern):
    
    with open(txt_file, "r", encoding="utf-8") as file:
        content = file.read()
        txt_list.append(content)
pprint(txt_list)

with open(txt_out, "w", encoding="utf-8") as file:
    for txt in txt_list:
        txt = txt.replace(".", ". \n")
        file.write(txt + "\n"+"\n")