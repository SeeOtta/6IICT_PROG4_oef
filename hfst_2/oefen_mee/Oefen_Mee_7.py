import csv

fp = open( "Leerkracht_Bestanden/6IICT_PROG4_oef/hfst_2/oefen_mee/volcanic-eruptions-EU.csv", "r" )
csv_reader = csv.DictReader( fp , delimiter=";")

eruptions_ld = [] # ld = lijst van dictionaries
for rij in csv_reader:
    print(rij)
    eruptions_ld.append(rij)

fp.close() # Na sluiten is CSV niet meer bruikbaar

print("")
print(eruptions_ld)

eruptions_ld_verwerkt = []

for index, rij in enumerate(eruptions_ld):
    dic = {}
    dic["Year"] = abs(int(rij["Year"]))
    dic["Name"] = rij["Name"].lower()
    eruptions_ld_verwerkt.append(dic)

print(eruptions_ld_verwerkt)

fp = open( "Leerkracht_Bestanden/6IICT_PROG4_oef/hfst_2/oefen_mee/eruptions_ld_verwerkt.csv", "w", newline="")
csv_writer = csv.DictWriter(fp, delimiter=";", fieldnames=["Year", "Name"])

csv_writer.writeheader()
for rij in eruptions_ld_verwerkt:
    csv_writer.writerow(rij)

fp.close()

