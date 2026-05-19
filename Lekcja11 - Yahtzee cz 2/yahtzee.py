import random

nazwy_punktow = ["Jedynki", "Dwójki", "Trójki", "Czwórki", "Piątki", "Szóstki"]
wartosci = ["---"] * 6 # ["---", "---", "---", "---", "---", "---"]

kosci = [4, 3, 5, 2, 1] # od 0 do 4

# Zadanie dodatkowe: proszę ocenić jaką wartość domyślną mogłyby mieć numery_kosci
def rzut_koscmi(numery_kosci: str): # np. '124'
    for numer in numery_kosci: # od 1 do 5
        indeks = int(numer) - 1
        kosci[indeks] = random.randint(1, 6)


def pokaz_kosci():
    print('___________________')
    for i in range(5): # od 0 do 4
        print(f"{i+1}: {kosci[i]}") # kości od 1 do 5


def pokaz_wyniki():
    print('___________________')
    for i in range(6):
        print(f"{nazwy_punktow[i]}\t{wartosci[i]}")


def czy_przerzucamy() -> bool:
    odp = input("Czy chcesz przerzucać kości? ")
    if odp in ["t", "T", "tak", "TAK", "Tak"]:
        return True
    return False


rzut_koscmi('54321')
pokaz_kosci()

for i in range(2):
    czy_przerzut = czy_przerzucamy()

    if czy_przerzut:
        kosci_do_przerzutu = input("Wypisz numery kości do przerzutu - bez spacji. ") # '1345'
        rzut_koscmi(kosci_do_przerzutu)
        pokaz_kosci()

    else:
        break