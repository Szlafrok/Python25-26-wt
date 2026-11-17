# import random as ra -> ra.randint()
# import random       -> random.randint()

from random import randint

kosci = [2, 3, 1, 4, 5]
nazwy_wynikow = ["Jedynki", "Dwójki", "Trójki", "Czwórki", "Piątki", "Szóstki"]
wyniki = [None, None, None, None, None, None]

def pokaz_kosci(kosci):
    for i in range(5):
        print(f"{i+1}. {kosci[i]}")
    print("----------------")


def czy_przerzucamy():
    odp = input("Czy chcesz przerzucać? T/N: ")
    if odp == 'T' or odp == 't':
        return True
    else:
        return False

def rzuc_koscmi(przerzucone = "12345"):
    for kosc in przerzucone:
        kosci[int(kosc)-1] = randint(1, 6)


def wypisz_wyniki():
    for i in range(6):
        print(f"{nazwy_wynikow[i]}: {wyniki[i]}")
    print("----------------")

wypisz_wyniki()

print(kosci)
rzuc_koscmi()

print(czy_przerzucamy())
pokaz_kosci(kosci)


for i in range(2):
    czy_rzut = czy_przerzucamy() # Zadanie za plusa: proszę tę i następną linijkę zapisać w jednej
    if czy_rzut:
        kosci_do_rzutu = input("Podaj numery kości do przerzucenia (bez spacji): ")
        rzuc_koscmi(kosci_do_rzutu)
        pokaz_kosci(kosci)
    else:
        break

