import csv        #iporteer csv

fp = open( "volcanic-eruptions-EU.csv", "r" )      #open bestand als read modus
# var csv_reader kan je niet rechtstreeks wijzigen of oproepen.
csv_reader = csv.reader( fp , delimiter=";")       #Lees het bestand en deel de zin op na elke ;
# print(csv_reader[3]) # Voorbeeld

# Aanmaken ECHTE lijst van lijsten (ll) en hierin gegevens stoppen
eruptions_ll = []                                  #een lege lijst maken
for rij in csv_reader:                             #doorloop alle rijen in csv_reader
    eruptions_ll.append(rij)                       #voeg alle rij toe aan lege lijst

fp.close() # Na sluiten is CSV niet meer bruikbaar

for eruption in eruptions_ll:                      #zet de lijst om
    print(eruption)                                #print de lijst