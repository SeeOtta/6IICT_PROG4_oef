import _json
import json

fp = open("Leerkracht_Bestanden/6IICT_PROG4_oef/hfst_2/oefen_mee/oefenmee9.json", "r")
quiz = json.load(fp)
fp.close()