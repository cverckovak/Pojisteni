from novy_uzivatel import Pojistenec
class Databaze:

    pojistenci = []

    def __init__(self):
        self.pojistenci = []

    def __str__(self):
        return f"{self.pojistenci}"

    def pridej_pojistence(self, jmeno, prijmeni, vek, cislo):
        novy_pojistenec = Pojistenec(jmeno, prijmeni, vek, cislo)
        self.pojistenci.append(novy_pojistenec)

    def vrat_pojistence(self):
        return self.pojistenci






