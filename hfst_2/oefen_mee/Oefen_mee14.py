import json, requests

antwoord = requests.get("https://api.covid19api.com/dayone/country/belgium/status/confirmed").text
antwoord_dict = json.loads(antwoord)   #vorm antwoord (string in JSON-formaat) om naar de dict antwoord te zetten
print(antwoord)


