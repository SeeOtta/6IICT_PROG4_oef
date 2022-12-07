import requests, json

client_id = "Vervang door eigen client id (string)"
client_secret = "vervang door eigen client secret (string)"

# Herinner je dat een API gewoon een speciale URL is...
# Via deze URL kunnen we ons inlogtoken aanvragen.
url = 'https://accounts.spotify.com/api/token'

# Deze zaken moeten we de API geven om een inlogtoken te genereren.
inloggegevens = {
    'grant_type': 'client_credentials',
    'client_id': '162d1866abfd41969e04a30571f62986',
    'client_secret': 'f0ead3602bef4e5db0c8591b0a26ede0'
}

# requests het inlogtoken, haal de tekst uit deze request en zet in cred_response
cred_resp = requests.post(url, inloggegevens).text
# Opgelet! Onderstaande regel is BELANGRIJK. 
cred_resp = json.loads(cred_resp)

print(type(cred_resp))

""" Oefen mee 2: 
zet de dictionary cred_resp in JSON-bestand met de naam certificatie.json

"""

fp = open("Leerkracht_Bestanden/6IICT_PROG4_oef/hfst_2/spotify_api/certificatie.json", "w")
fp.write(str(cred_resp))
fp.close()