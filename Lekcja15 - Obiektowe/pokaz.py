class Pies:
    imie = ""
    rasa = ""
    wiek = 0
    nasycenie = 100

    def jedz(self):
        print("Om nom nom zajadam karkowke")
        self.nasycenie += 20

    def wyswietl_wiek(self):
        print(f"Pies imieniem {self.imie} ma {self.wiek} lat")

    def ustaw_wiek(self, wiek): # setter
        self.wiek = wiek

    def pozyskaj_wiek(self): # getter
        return self.wiek


pies = Pies()

pies.imie = "Fafik"
pies.rasa = "Owczarek szatlandzki"
pies.wiek = 4

print(pies.imie, pies.rasa, pies.wiek, pies.nasycenie)

pies.jedz()

print(pies.nasycenie)
pies.wyswietl_wiek()

pies.ustaw_wiek(10)
pies.wyswietl_wiek()

print(pies.pozyskaj_wiek())