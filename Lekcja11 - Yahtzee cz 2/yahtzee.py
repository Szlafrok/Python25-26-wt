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


def wybierz_pole_punktowe():
    wybrane_pole = int(input("Podaj numer pola, które chcesz zająć (1-6): ")) # od 1 do 6
    while wartosci[wybrane_pole - 1] != "---":
        wybrane_pole = int(input("Podaj numer pola, które chcesz zająć (1-6): "))
    return wybrane_pole

def policz_punkty(numer_pola):
    wynik = 0

    for kosc in kosci: # for i in range(5)
        if kosc == numer_pola: # if kosci[i] == numer_pola
            wynik += kosc # kosci[i]

    return kosc

    # Utwórz zmienną "wynik" o wartości 0
    # Za pomocą pętli for przejdź po każdej wartości w kościach:
        # Jeżeli wartość kości jest równa numerowi pola:
            # Zwiększ wynik o wartość tej kości
    # Zwróć zmienną wynik

rzut_koscmi('54321')
pokaz_kosci()

while True:
    for i in range(2):
        czy_przerzut = czy_przerzucamy()

        if czy_przerzut:
            kosci_do_przerzutu = input("Wypisz numery kości do przerzutu - bez spacji. ") # '1345'
            rzut_koscmi(kosci_do_przerzutu)
            pokaz_kosci()

        else:
            break

    pokaz_wyniki()
    pole = wybierz_pole_punktowe() # od 1 do 6
    wartosci[pole - 1] = policz_punkty(pole)

    if not "---" in wartosci:
        break

print(f"{sum(wartosci)} - końcowy wynik")