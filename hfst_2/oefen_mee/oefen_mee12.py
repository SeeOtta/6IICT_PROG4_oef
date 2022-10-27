import json

fp = open("Leerkracht_Bestanden/6IICT_PROG4_oef/hfst_2/oefen_mee/oefen_mee12.json", "r")
dag = json.load(fp)
fp.close()  # Na sluiten is JSON niet meer bruikbaar

gekozen_dag = input("Geef een dag ")
print(f"Op {gekozen_dag} heb je volgende activiteiten ingepland : ")
for item in dag[gekozen_dag]:
    print(item)
    activiteiten = {item}

verander = input(str("Wil je iets aanpassen? (j/n) "))
if verander == str("j"):
    print("jippie")
    wijziging = input(str("Wat wil je inplannen? "))
    activiteiten.pop()
    activiteiten = (wijziging)
    print(activiteiten)
    opnieuw = input(str("Nog iets? (j/n) "))
    if opnieuw == str("j"):
        wijziging2 = input(str("Wat wil je inplannen? "))
        activiteiten = (wijziging , wijziging2)
        print(f"{activiteiten} staan ingepland op {gekozen_dag}")
    else:
        print("Oke")
else:
    print("Oke")
fp = open("Leerkracht_Bestanden/6IICT_PROG4_oef/hfst_2/oefen_mee12.json", "w")
for item in dag[gekozen_dag]:
    item = activiteiten
fp.close()
