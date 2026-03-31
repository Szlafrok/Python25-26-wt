liczba = 0.1
liczba2 = 0.2
print(liczba + liczba2)

# Za pomocą Copilota proszę dowiedzieć się, jak działa
# mnożenie stringów i za jego pomocą wypisać tekst:

# AAAAABBBBBAAAAABBBBBAAAAABBBBB

print("AAAAABBBBB" * 3)
print(("A" * 5 + "B" * 5) * 3)

# km/h -> m/s

predkosc = 72

wynik = predkosc * 1000 # m/h 
wynik = wynik / 3600 # m/s

# print(predkosc * 1000 / 3600)
# print(predkosc / 3.6)

print(wynik)

#################################

a = 3
b = 5

# + - * /

wynik = a + b
print(wynik)

wynik = a - b
print(wynik)

wynik = a * b
print(wynik)

wynik = a / b
print(wynik)

print("----------------")

a = 3
b = 5

wynik = a
wynik += b # wynik = wynik + b
print(wynik) # 8

wynik -= a # wynik = wynik - a
print(wynik) # 5

wynik *= b # wynik = wynik * b
print(wynik) # 25

wynik %= b*b # wynik = wynik % (b*b)
print(wynik)