"""Word Count Tutorial"""
import re
from pathlib import Path
from own_packages import path_attributes as pa   # pylint: disable=import-error


DATA_PATH = pa.SOURCE_DIR
DATA_PATH = Path(DATA_PATH)
TXT_FILES_PATH = DATA_PATH / 'txt_files'




def main():
    """Main function"""
    words_list = []
    for files in TXT_FILES_PATH.iterdir():
        if files.is_file():
            with open(files, 'r', encoding="utf-8") as file:
                file_text = file.read()
                words_list.append( file_text.split())
    words_list = [  words.strip(".,") for sublist in words_list for words in sublist]
    words_list =  [re.sub(r',\[\d+\]', '', word) for word in words_list]
    print(words_list)


    word_dict = {}
    for word in words_list:
        if not word  in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1


    print(word_dict)

if __name__ == '__main__':
    main()
