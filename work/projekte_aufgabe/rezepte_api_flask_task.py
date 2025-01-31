"""Aufgabe Flask"""
from flask import Flask

recipes = {
1: {'id': 1, 'title': 'Spaghetti Carbonara',
    'ingredients': ['spaghetti', 'eggs', 'pecorino cheese', 'guanciale'],
    'instructions': 'Cook pasta, fry guanciale, mix with eggs and cheese, and combine with pasta.'},
2: {'id': 2, 'title': 'Tomato Soup',
    'ingredients': ['tomato', 'water', 'salt'],
    'instructions': 'Boil all together until mushy, blend, and serve.'},
    3: {'id': 3, 'title': 'Grilled Cheese Sandwich',
        'ingredients': ['bread', 'cheese', 'butter'],
        'instructions': 'Butter bread, place cheese between slices, grill until golden.'}
}
app = Flask(__name__)

@app.route("/recipes/<id_r>")
def get_rezept(id_r):
    """Funktion um den Rezepte-Wert zu bekommen."""
    id_r = int(id_r)
    rezept = recipes.get(id_r)
    if rezept:
        return rezept
    return f"{id_r} is out of Range"


@app.route("/")
def index():
    """Funktionalität damit überhaupt gestreamt wird"""
    return "Homepage"

app.run()
