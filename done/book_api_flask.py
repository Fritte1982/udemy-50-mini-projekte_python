from flask import Flask
import json

app = Flask(__name__)

json_path: str = (
    r"C:\Users\richa\git-projekte\udemy-50-mini-projekte_python\files_data\books.json"
)

with open(json_path) as file:
    books = json.load(file)
    
@app.route("/books/<book_id>")
def get_book(book_id):
    book =books.get(book_id)
    if book:
        return book
    else:
        return {'message': 'Book not found'}, 404

@app.route("/")
def index():
    return "Homepage"


app.run(debug=True)