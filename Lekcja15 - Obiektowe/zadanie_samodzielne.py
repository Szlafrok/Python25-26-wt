# Proszę napisać klasę Gracz. Każdy gracz ma:

# CECHY
# - nazwę użytkownika (username)
# - poziom zdrowia (health)
# - siła (power)

# METODY
# - upadek(self): zadaje 5 obrażeń od upadku i pisze "AUA"
# - ustaw_sile(self, sila): SETTER siły (ustawia siłę gracza)
# - pozyskaj_sile(self): GETTER siły (zwraca siłę gracza)

class Gracz:
    nazwa = ""
    zdrowie = 100
    sila = 100

    def upadek(self):
        self.zdrowie -= 5
        print("AUA MOJE KOLANO")

    def ustaw_sile(self, sila):
        self.sila = sila

    def pozyskaj_sile(self):
        return self.sila
    
gracz = Gracz()
gracz.nazwa = "Szlafrok"
gracz.sila = 100
gracz.zdrowie = 100

gracz.upadek()
gracz.ustaw_sile(9000)
print(gracz.pozyskaj_sile())


# Czym jest klasa - WOJTEK ++
# Czym jest obiekt - ULA +++
# Czym jest metoda - PIOTREK
# Czym jest cecha - JULKA ++
# Czym jest getter i setter - STEFAN ++++
# Po co nam self w metodach? - ZUZIA +++