class Hond:

    def benoem(self, benaming):
        self.naam = benaming

    def weegen(zelf, weging):
        zelf.weeg = weging

    def blaf(self):
        print(f"{self.naam} zegt woof")

    def weegschaal(self):
        print(f"{self.naam} weegt {self.weeg} kg")

hond = Hond()
hond.benoem("Joostje")
hond.blaf()
hond.weegen(2)
hond.weegschaal()

huisdier = Hond()