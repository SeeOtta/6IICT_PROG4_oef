import _json
import json

fp = open("Leerkracht_Bestanden/6IICT_PROG4_oef/hfst_2/oefen_mee/oefenmee8.json", "r")
dag = json.load(fp)
fp.close()  # Na sluiten is JSON niet meer bruikbaar

gekozen_dag = input("Geef een dag ")

for item in dag[gekozen_dag]:
    print(item)