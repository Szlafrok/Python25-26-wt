liczby = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print(len(liczby))

for liczba in liczby:
    print(liczba ** 2)

# -----------

for i in range(3, 8, 2): # od 3 włącznie do 8 WYŁĄCZNIE z krokiem co 2
    print(i) # 3, 5, 7

# ZADANIE SAMODZIELNE

# 1. Proszę zaprogramować takie samo wypisanie kwadratów liczb parzystych od 2 do 20,
# ale z wykorzystaniem funkcji range() zamiast listy.

for i in range(2, 22, 2): # ... 16, 18, 20
    print(i ** 2)




# 2*. Proszę utworzyć listę, która zawierać będzie 50 zer
lista = [0] * 50

# 3*. Proszę napisać program, który za pomocą pętli zsumuje wszystkie liczby
# zawarte w liście. Można założyć, że lista zawiera wyłącznie liczby.
suma = 0
for liczba in liczby:
    suma += liczba