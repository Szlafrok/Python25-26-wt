dzien = int(input())

if dzien == 1:
    print("poniedziałek")
elif dzien == 2:
    print("wtorek")
elif dzien == 3:
    print("środa")
elif dzien == 4:
    print("czwartek")
elif dzien == 5:
    print("piątek")
elif dzien == 6:
    print("sobota")
else:
    print("niedziela")


# jeżeli dzień = 1 to wypisz poniedziałek
# w przeciwnym razie jeżeli dzień = 2 to wypisz wtorek
# w przeciwnym razie jeżeli dzień = 3 to wypisz środa
# w przeciwnym razie jeżeli dzień = 4 to wypisz czwartek
# w przeciwnym razie jeżeli dzień = 5 to wypisz piątek
# w przeciwnym razie jeżeli dzień = 6 to wypisz sobota
# w przeciwnym razie wypisz niedziela



# Zadanie samodzielne (++)
# Proszę do zmiennej 'kolor' wpisać literę "R" (red - czerwony), "Y" (yellow - żółty), "G" (green - zielony)
# Napisz program, który na podstawie zmiennej kolor powie, czy trzeba się zatrzymać, przygotować czy ruszać.

color = input("Podaj kolor: ")

if color == "R":
    print("STÓJ PRRRRRRRRRRRRR CZERWONE JEST")
elif color == "Y":
    print("PRZYGOTUJ SIĘ WBIJ SOBIE JEDYNKĘ CZY COŚ")
else:
    print("ZIELONE CIŚNIEMY JUHUUUUUUUUUUUUU")


# Zadanie samodzielne II (+++)
# Proszę napisać program, który wczyta od użytkownika liczbę reprezentującą dzień tygodnia i:
# Jeśli liczba jest w przedziale od 1 do 5, wypisze że nie ma weekendu
# Jesli liczba jest równa 6 lub 7, wypisze że jest weekend
# W przeciwnym razie powie, że mamy błędny dzień tygodnia

dzien = int(input("Podaj dzień tygodnia"))

if 0 < dzien and dzien <= 5: # 0 < dzien <= 5
    print("nie ma weekendu")
elif dzien == 6 or dzien == 7:
    print("jest weekend")
else:
    print("a co to za dzień tygodnia w ogóle????")