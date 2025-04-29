"""Aufgabe um Länder-Daten zu extrahieren."""
from pprint import pprint
import requests

country = input("Gib ein Land ein: ")
URL = f"https://restcountries.com/v3.1/name/{country}"

response = requests.get(URL, timeout=10)

raw_data = response.json()
pprint(f"Gewähltes Land: {country}")
pprint(f"Hauptstadt: {raw_data[0]['capital'][0]}")
pprint(f"Kontinent: {raw_data[0]['region']}")
pprint(f'Bevölkerung: {raw_data[0]["population"]}')
sprache =raw_data[0]["languages"].values()
SPRACHEN = ", ".join(sprache)
pprint(f"Sprachen: {SPRACHEN}")
