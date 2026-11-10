# import random as ra -> ra.randint()
# import random       -> random.randint()

from random import randint

kosci = [2, 3, 1, 4, 5]

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

print(czy_przerzucamy())

    # Proszę uzupełnić definicję funkcji czy_przerzucamy tak, aby
    # - wczytywała od użytkownika odpowiedź na pytanie czy przerzucamy
    # - jeśli odpowiedź brzmi 't' lub 'T' - zwracamy True
    # - w przeciwnym razie zwracamy False

    # Bonus bazowy +++
    # [*] + wykorzystanie .upper() lub .lower()
    # [*] + proszę to zrobić w jednej linijce :D

# pokaz_kosci(kosci)

