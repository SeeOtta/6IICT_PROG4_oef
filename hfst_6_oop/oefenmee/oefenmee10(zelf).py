import random

class Hond:
    locaties = ["badkamer", "straat", "slaapkamer", "living", "gang"]
    def __init__(self, naam):
        self.naam = naam
        self.locatie = random.choice(self.locaties)

    def ziet_hond(self, andere_daggoe):
        if self.locatie == andere_daggoe.locatie:
            print(f"{self.naam} ziet {andere_daggoe.naam} in/op de {self.locatie}")
            
            nieuw = random.choice([self,andere_daggoe])
            nieuw.locatie = random.choice(self.locaties)
            print(f"{nieuw.naam} is bang en rent naar de {nieuw.locatie}")
        else:
            print(f"{self.naam} ziet geen andere hond in/op de {self.locatie}.")

hond1 = Hond("Poentje")
hond2 = Hond("Quinten")
hond3 = Hond("Koen")

hond1.ziet_hond(hond2)
hond1.ziet_hond(hond3)
hond2.ziet_hond(hond3)
