"""Eine Datei auf Dropbox laden"""
import os
import sys
import dropbox
import dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from own_packages import path_attributes as pa

SOURCE_PATH = pa.SOURCE_DIR
file_path = SOURCE_PATH + r"\employee_data (1).xlsx"

dotenv.load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
d= dropbox.Dropbox(ACCESS_TOKEN)

with open (file_path, "rb" ) as file:
    content =file.read()
    d.files_upload(content, '/employee_data (1).xlsx', mode=dropbox.files.WriteMode('overwrite'))
    print(f"Success {file_path} upload")
