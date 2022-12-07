import requests, json

""" Oefen mee 3:
Haal de dictionary op uit credentials.json.

Zet de waarde van de key "access_token" (de zeer lange string),
in de variabele wachtwoord.
"""
fp=open("Leerkracht_Bestanden/6IICT_PROG4_oef/hfst_2/spotify_api/certificatie.json", "r")
info = json.load(fp)
wachtwoord = info["access_token"]
print(wachtwoord)

""" Oefen mee 4:
Vul url aan om de data van het lied op te halen.
"""
headers = {
    "Authorization": f"Bearer {wachtwoord}"
}
track_id = '6XnTftNvSj8mvYxoYB6a5j'
url = f"https://api.spotify.com/v1/tracks/{track_id}"

lied = requests.get(url, headers=headers).text
lied = json.loads(lied)

""" Oefen mee 5:
Zet de variabele lied in een JSON-bestand lied.json.

Welk lied heb je net opgehaald?

Pas de dictionary aan door de keys "available markets" te verwijderen.
Schrijf de dictionary HIERNA pas weg naar een JSON-bestand.
"""

fp=open("Leerkracht_Bestanden/6IICT_PROG4_oef/hfst_2/spotify_api/lied.json", "w")
fp.write(str(lied))
fp.close()
