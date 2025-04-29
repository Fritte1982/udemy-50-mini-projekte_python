"""Die Historischen Ereignisse des Datums """
from pprint import pprint
import requests

day_in = input("Input a day-number:  ")
month_in = input("Input a Month-Number: ")

day = day_in
month = month_in

URL = f"https://history.muffinlabs.com/date/{month}/{day}"

response = requests.get(URL, timeout=10)
data = response.json()

events =data["data"]["Events"]

for event in events:
    pprint(f"Im Jahr: {event['year']}")
    print(f"Ist folgendes passiert: {event['text']}")
    pprint(f"Mehr Informationen: {event['links'][0]['link']}")
    print("\n")
