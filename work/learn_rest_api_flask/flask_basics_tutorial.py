"""First Recipe API"""
import json
from os import path
from flask import Flask
from own_packages import path_attributes as pa

in_book_json = path.join(pa.SOURCE_DIR, "books.json")

app = Flask(__name__)

with open(in_book_json, encoding="utf-8") as file:
    books = json.load(file)

@app.route("/books/<book_id>")
def get_book(book_id):
    """Gibt einen String oder den Dict-Wert zurück"""
    try:
        book = books[book_id]
    except KeyError:
        return "Sorry Book-ID is out of range "
    return book

@app.route("/")
def index():
    """Funktionalität damit überhaupt gestreamt wird"""
    return "Homepage"

app.run()
