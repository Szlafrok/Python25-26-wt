import random

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

rzut_koscmi('54321')
pokaz_kosci()