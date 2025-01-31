from os import path

FILE_PATH = __file__
WORK_PATH = path.dirname(FILE_PATH)
PROJECT_PATH = path.dirname(WORK_PATH)
SOURCE_DIR = path.join(PROJECT_PATH,"files_data")
SOURCE_XLSX= path.join(PROJECT_PATH, "files_data","employee_data (1).xlsx")
OUTPUT_PATH = path.join(PROJECT_PATH,"output")

if __name__ == '__main__':
    print(SOURCE_DIR)