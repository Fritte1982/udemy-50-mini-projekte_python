import os
import sys
import dropbox
import dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from own_packages import path_attributes as pa

SOURCE_PATH = pa.SOURCE_DIR

ENV_PATH = r"C:\Users\richa\git-projekte\udemy-50-mini-projekte_python\work\DropBox_API\.env"
dotenv.load_dotenv(ENV_PATH)
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
d= dropbox.Dropbox(ACCESS_TOKEN)

for i in os.listdir(SOURCE_PATH):
        dateipfad = os.path.join(SOURCE_PATH, i)
        if os.path.isfile(dateipfad):
            with open(dateipfad, "rb") as file:
                content = file.read()
                d.files_upload(content, f'/{i}', mode=dropbox.files.WriteMode('overwrite'))
                print(f"Success {dateipfad} upload")