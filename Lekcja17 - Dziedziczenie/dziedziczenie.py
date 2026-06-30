class Miecz():
    def __init__(self, wlasciciel, obrazenia):
        self.wlasciciel = wlasciciel
        self.obrazenia = obrazenia

    def przedstaw_sie(self):
        print(f"Należę do {self.wlasciciel} i zadaję {self.obrazenia} obrażeń.")

    def szpanuj(self):
        print("Jestem mieczem! Tak po prostu")

class Katana(Miecz):
    def __init__(self, wlasciciel, obrazenia):
        super().__init__(wlasciciel, obrazenia) # odwołanie do konsturktora klasy wyższej

    # metoda przedstaw_sie jest taka sama, więc nie muszę jej powtarzać

    def szpanuj(self): # nadpisanie metody
        print("Jestem japońskim mieczem samuraja!")

katana = Katana("Piotrek", 10)
katana.przedstaw_sie()
katana.szpanuj()


class Szabla():
    def __init__(self, wlasciciel, obrazenia):
        super().__init__(wlasciciel, obrazenia)

    def szpanuj(self):
        print("Kończ waść, wstydu oszczędź!")