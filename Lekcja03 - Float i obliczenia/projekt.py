wiek = "14"
imie = "Janek"

wiek = int(wiek)

# wiek = int(input("Ile masz lat? "))
# print(wiek - 1)

# print(f"Mam na {imie} imię i mam {wiek} lat")

# --------------------------------------

liczba = 20.4
liczba_2 = 10.0


int() # Zamiana na INT
str() # Zamiana na STR

float()

x = float("123")
print(x)

x = float("12.3")
print(x)

# x = float("sosnowiec") BŁĄD!
# print(x)

x = 12.8

y = int(x)
print(y)

y = str(x)
print(y)

# ---------------------------------

x = 15
y = 67

# Dodawanie
wynik = x + y
print(f"Dodawanie: {wynik}")

# Odejmowanie
wynik = y - x
print(f"Odejmowanie: {wynik}")

# Mnożenie
wynik = x * y
print(f"Mnożenie: {wynik}")

# Dzielenie
wynik = y / x # x = 15, y = 67
print(f"Dzielenie: {wynik}")

x = 2
y = 5
# Potęgowanie
wynik = x ** y
print(f"Potęgowanie: {wynik}")

# Pierwiastkowanie
wynik = x ** 0.5
print(f"Pierwiastek: {wynik}")

import math
wynik = math.sqrt(x)
print(f"Pierwiastek: {wynik}")


# Dzielenie z resztą: 5 : 2 = 2, r. 1
wynik = y % x
print(f"Reszta z dzielenia: {wynik}")

# Dzielenie całkowite
wynik = y // x
print(f"Dzielenie całkowite: {wynik}")
