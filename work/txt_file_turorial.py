from own_packages import path_attributes as pat
from pathlib import Path
from pprint import pprint

sources_dir = Path(pat.SOURCE_DIR)
txtfiles_dir = sources_dir / "txt_files"
output_dir = Path(pat.OUTPUT_PATH)
txtfile_out = output_dir / "word_counts.txt"

all_words = []
for txt_file in txtfiles_dir.glob("*.txt"):
    with open(txt_file, "r", encoding="utf-8") as file:
        text = file.read()
        word_list = text.split()
        for word in word_list:
            word =word.rstrip(".")
            word = word.rstrip(",")
            all_words.append(word)

unique_words =set(all_words)

words_dict = {}



count = 0 
for word in all_words:
    if word in words_dict:
        count += 1
        words_dict[word] +=1
    else:
        words_dict[word] = 1

pprint(words_dict)
with open(txtfile_out, "w", encoding="utf-8") as file:
    pass
for key, value in words_dict.items():
    with open(txtfile_out, "a+", encoding="utf-8") as file:
        file.write(f"{key}: {value}"+ "\n")