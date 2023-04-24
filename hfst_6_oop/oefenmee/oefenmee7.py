class Hond:
    naam = "Lucky"
    massa = 5

    def benoem(self, benaming):
        naam1 = self.naam
        self.naam = benaming
        print(f"{naam1} heet nu {self.naam}")

    def weegen(zelf, weging):
        zelf.weeg = weging

    
    def eten(self, hoeveelheid):
        self.massa = self.massa + (0.3* hoeveelheid)
        print(f"{self.naam} weegt {self.massa} kg")

hond = Hond()
hond.benoem("Ziyaad Wahibibi")
hond.eten(0.5)
hond.eten(0.5)
hond.eten(0.5)

hond2 = Hond()
hond2.benoem("Fleur")
hond2.eten(0.5)
hond2.eten(0.5)
hond2.eten(0.5)