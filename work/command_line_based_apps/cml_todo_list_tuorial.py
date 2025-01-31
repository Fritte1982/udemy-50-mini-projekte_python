"""Der Klassiker ein Todo-list"""
import locale
import os
import sys
from datetime import datetime as dt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from own_packages import path_attributes as pa
locale.setlocale(locale.LC_ALL, 'deu_deu')
OUTPUT_PATH = pa.OUTPUT_PATH

todo_liste =[]
while 1:
    todo_row: str = input(
        "Bitte Ihre Aufgaben für Heute eingeben (Tippe 'done' um die Eingabe zu beenden): "
    )
    if todo_row == 'done':
        break
    todo_liste.append(todo_row)

day = dt.now().strftime("%A")
file_path = OUTPUT_PATH + rf'\{day}.txt'

with open(file_path, "w", encoding= "utf-8") as file:
    if todo_liste:
        content = "\n".join(todo_liste)
        file.write(content)
        print(f"Ihre Aufgaben wurden in den Datei-Pfad {file_path} gespeichert. ")
    else:
        print("Nichts zu speichern, in der Aufgaben-Liste! ")
