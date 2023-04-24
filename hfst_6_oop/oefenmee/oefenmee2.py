class Hond:
    naam = "wafel"
    massa = "veel"


    def blaf(self):
        print(f"{self.naam} zegt woof")

    def weegschaal(zichzelf):
        print(f"{zichzelf.naam} weegt {zichzelf.massa}")

hond = Hond()
huisdier = Hond()

print(f"datatype hond: {type(hond)}")
print(hond.naam)
print(hond.massa)
hond.blaf()
hond.weegschaal()
print(f"datatype huisdier: {type(huisdier)}")
print(huisdier.naam)
print(huisdier.massa)
huisdier.blaf()
huisdier.weegschaal()


#niv 3: omdat het in de class zit dus gebruikt daar de waardes van