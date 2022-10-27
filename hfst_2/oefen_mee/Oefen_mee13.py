import json


fp = open("Leerkracht_Bestanden/6IICT_PROG4_oef/hfst_2/oefen_mee/Oefen_mee13.json", "r")
data = json.load(fp)
fp.close()
dic_corona = {}
dic_corona = data

for index, dag in enumerate(dic_corona):
    if index == 0:
        dag1 = int(dag["Cases"])
        print(f"{dag['Date']} zijn er 0 nieuwe cases.")
    else:
        verschil = dag["Cases"] - aantal_vorige_dag
        print(f"op {dag['Date']} zijn er {verschil} nieuwe cases")
        dic_corona[index]["Nieuwe Cases"] = verschil
    aantal_vorige_dag = dag["Cases"]

fp = open("Leerkracht_Bestanden/6IICT_PROG4_oef/hfst_2/oefen_mee/Oefen_mee13.json", "w")
json.dump(dic_corona, fp)
fp.close()








