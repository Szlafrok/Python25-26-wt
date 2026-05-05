print(123)

print(round(5.8))

def heheszki(tresc):
    print(f"Ale śmiesznie! {tresc}")

heheszki("XD")
heheszki("HAHAHA")


def sumuj(x, y):
    print(x + y)

# sumuj(5) - za mało argumentów
# sumuj(1, 2, 3) - za dużo argumentów

sumuj(5, 7)
sumuj("5", "7")


# ZADANIE SAMODZIELNE
# Proszę napisać funkcje, która przyjmuje jako argumenty boki 
# prostokąta 'a' i 'b', a następnie wypisuje obwód tego prostokąta
# i jego pole.

# Obwód wyrażamy wzorem 2*a + 2*b, pole jest równe a*b.

# 1. Napisać definicję funkcji
# 2. Określić w tej definicji 2 argumenty
# 3. Napisać odpowiednie printy, które wypiszą wynik.

from math import sqrt

def trojkat_prostokatny(a, b):
    print(f"Pole trójkąta to {a * b / 2}")
    print(f"Obwód trójkąta to {a + b + sqrt(a**2 + b**2)}")

trojkat_prostokatny(3, 4)