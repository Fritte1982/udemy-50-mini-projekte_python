from os import path
from pathlib import Path

FILE_PATH = __file__
WORK_PATH = path.dirname(FILE_PATH)
PROJECT_PATH = path.dirname(WORK_PATH)
SOURCE_DIR = path.join(PROJECT_PATH,"files_data")
SOURCE_DIR = Path(SOURCE_DIR)
SOURCE_XLSX= path.join(PROJECT_PATH, "files_data","employee_data (1).xlsx")
OUTPUT_PATH = path.join(PROJECT_PATH,"output")
OUTPUT_PATH = Path(OUTPUT_PATH)
DOCX_SOURCE =  Path(SOURCE_DIR) /  "word_documents_sources"


if __name__ == '__main__':
    if SOURCE_DIR.exists():
        print(SOURCE_DIR)