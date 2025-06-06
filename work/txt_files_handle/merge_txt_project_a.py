from pathlib import  Path
from own_packages import path_attributes as pa

OUTPUT = pa.OUTPUT_PATH
OUTPUT = Path(OUTPUT)
TXT_IN_PATH = pa.SOURCE_DIR / "txt_files"

txts_list = []
for txt_file in TXT_IN_PATH.glob("*.txt"):
    with open(txt_file, "r", encoding="utf-8") as f:
        txt = f.read()
        txts_list.append(txt)

txt_output = OUTPUT / "merge_b.txt"
with open(txt_output, "w", encoding="utf-8") as f:
    for txt in txts_list:
        f.write(txt + "\n")

print (txts_list)
