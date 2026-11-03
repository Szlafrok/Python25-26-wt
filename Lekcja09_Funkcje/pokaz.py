def kanapka(): # DEFINICJA FUNKCJI
    print("Kroję chleb!")
    print("Smaruję masłem!")
    print("Nakładam szynkę!")
    print("Przykrywam kawałkiem chleba!")
    jedz()

def jedz():
    print("OM NOM NOM")
    
kanapka() # WYWOŁANIE FUNKCJI

print("-------------------------------")

def sumuj(a, b):
    print(f"Podano argumenty: a = {a}, b = {b}")
    print(f"Suma podanych liczb wynosi {a+b}")

sumuj(1, 9)

print("-------------------")

def wypisuj(tresc, ile = 1): # wartość domyślna argumentu
    for i in range(ile):
        print(tresc)

wypisuj("ciastko", 4)

wypisuj("ukulele")

wypisuj(ile = 3, tresc = "ugabuga")

# wypisuj(ile = 5, "slowo") TAK NIE ROBIMY!

