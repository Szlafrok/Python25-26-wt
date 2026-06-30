class Kot():

    def __init__(self, imie, wiek, rasa):
        self.imie = imie
        self.wiek = wiek
        self.rasa = rasa

    def daj_glos(self):
        print(f"[{self.imie}] miau")

kotek = Kot("Loki", 6, "Egipski Mau")

print(kotek.imie, kotek.wiek, kotek.rasa)
kotek.daj_glos()