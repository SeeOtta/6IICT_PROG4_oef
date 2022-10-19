import json

fp = open("Leerkracht_Bestanden/6IICT_PROG4_oef/hfst_2/oefen_mee/oefenmee9.json", "r")
quiz = json.load(fp)
fp.close()

print(quiz)

for key, onderwerp in quiz["quiz"].items():
    for key2, vraag in onderwerp.items():
       print(vraag["vraag"])
       print(vraag["opties"])
       beantwoord = input("Wat is het juiste antwoord?")
       if beantwoord == vraag["antwoord"]:
        print("Dit is juist")
       else:
        print("Fout")