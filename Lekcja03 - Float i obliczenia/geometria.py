# Proszę napisać program, który wczyta 2 liczby dziesiętne,
# które są bokami prostokąta. Zmienne powinny nazywać się a
# oraz b. 

# Prosze napisać program, który na podstawie tych zmiennych wyznaczy
# obwód tego prostokąta oraz jego pole.

# Obwód prostokąta = suma wszystkich boków
# Pole prostokąta = iloczyn wszystkich boków

a = float(input("Podaj bok a: "))
b = float(input("Podaj bok b: "))

obwod = (a + b) * 2
pole = a * b

print(f"Obwód wynosi {obwod}, a pole wynosi {pole}")