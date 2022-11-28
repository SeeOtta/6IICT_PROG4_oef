""" Niveau 1 & 2
Wat gaat hier mis?
"""
fruit_lijst = ["Appel", "Banaan", "Meloen", "Mango", "Druif"]
try:
    getal = int( input("Hoeveel fruit uit de lijst wil je printen: ") )
    for i in range(getal):
        fruit = fruit_lijst[i]
        print(fruit)
except IndexError:
    print("De opgegeven waarde is te groot.")
except ZeroDivisionError:
    print(f"Het getal 0 kan niet worden opgegeven.")
except ValueError:
    print(f"De ingegeven waarden is geen getal.")
except:
    print("onbekende fout opgetreden.")


""" Niveau 3 (haal uit commentaar) """
while True:
    fruit = input("Element aan lijst toevoegen: ")
    
    if fruit == "":
        break # Loop stopt wanneer gebruiker een lege string ingeeft.
    else:
        fruit_lijst.append(fruit)

print(fruit_lijst)
