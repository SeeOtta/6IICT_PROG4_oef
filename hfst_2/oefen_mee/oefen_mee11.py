import json

person_dict = {
    "naam": "Jan",
    "talen": ["Nl", "En"],
    "getrouwd": True,
    "leeftijd": 32}

# Maakt nieuw persoon.json aan in pad
fp = open("Leerkracht_Bestanden/6IICT_PROG4_oef/hfst_2/oefen_mee/oefen_mee11.json", "w")
json.dump(person_dict, fp)
fp.close() # Na sluiten is JSON niet meer bruikbaar