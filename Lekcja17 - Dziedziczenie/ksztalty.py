class Ksztalt(): # klasa po której dziedziczymy
    def __init__(self, kolor): # konstruktor bazowy
        self.kolor = kolor

    def pole(self): # pole (tylko szablon, bo nieznany kształt nie ma pola)
        return 0
    
    def opis(self): # bazowy opis
        print(f"Kształt w kolorze {self.kolor}")

class Kolo(Ksztalt):
    def __init__(self, kolor, promien):
        super().__init__(kolor) # kolor ustawiamy konstruktorem klasy wyższej
        self.promien = promien # ustalam NOWĄ cechę kształtu - promień koła

    def pole(self): # <- polimorfizm
        return self.promien ** 2 * 3.14 # ustalam pole koła na podstawie wzoru - pi r**2
    
    def opis(self): # nowy opis <- polimorfizm
        print(f"Jestem kołem o promieniu {self.promien} i kolorze {self.kolor}")

class Kwadrat(Ksztalt):
    def __init__(self, kolor, bok):
        super().__init__(kolor)
        self.bok = bok

    def pole(self):
        return self.bok ** 2
    
    def opis(self):
        print(f"Jestem kwadratem o boku {self.bok} i kolorze {self.kolor}")

class Prostokat(Ksztalt):
    def __init__(self, kolor, bok_1, bok_2):
        super().__init__(kolor)
        self.bok_1 = bok_1
        self.bok_2 = bok_2

    def pole(self):
        return self.bok_1 * self.bok_2
    
    def opis(self):
        print(f"Jestem prostokątem o bokach {self.bok_1} i {self.bok_2}, oraz o kolorze {self.kolor}")

figura = Prostokat("niebieski", 4, 5)
print(figura.pole())
figura.opis()
    

# 1. Proszę utworzyć klasę Kwadrat, która (+++)
#   - dziedziczy po klasie Kształt (więc automatycznie musi mieć też kolor)
#   - przyjmuje dodatkowy parametr - bok kwadratu "bok"
#   - w miejscu pole zwraca pole kwadratu bok ** 2
#   - w miejscu opisu mówi, że jest kwadratem o takim boku i takim kolorze

# 2. Proszę w analogiczny sposób utworzyć klasę Prostokat (+++)

# 3. Proszę utworzyć kilka obiektów i przetestować swój kod (++)