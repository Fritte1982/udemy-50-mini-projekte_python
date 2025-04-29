"""Abschnitt 7 Aufgabe"""
import locale
import os
import sys
from datetime import datetime as dt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from own_packages import path_attributes as pa
locale.setlocale(locale.LC_ALL, 'deu_deu')
OUTPUT_PATH = pa.OUTPUT_PATH

liste_mit_notizen = []
while 1:
    zeile_eingabe:str = input(
         "Geben Sie, Ihre Notizen für den Tag ein ('exit' für beenden und speichern ):"
     )
    if zeile_eingabe.lower() == 'exit':
         break
    liste_mit_notizen.append(zeile_eingabe)

day = dt.now().strftime("%A")
file_path: str = OUTPUT_PATH + rf"\{day}.txt"

with  open(file_path , "w", encoding="utf-8") as f:
    inhalt = "\n".join(liste_mit_notizen)
    f.write(inhalt)

with open(file_path, "r", encoding="utf-8") as file:
    cont = file.read()
print(cont)
