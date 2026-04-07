kolory = ["fioletowy", "czerwony", "niebieski", "zielony", "czarny"]

for k in kolory:
    print(k)
print("aaaaaaa" + k)

print("----------------------------------------------------")

produkty = ["mysz", "płatki", "chleb", "zmywarka", "kebab"]
ceny = [249.00, 7.50, 3.49, 1699.99, 10.25]

for p in produkty:
    print(f"Produkt: {p}")

for c in ceny:
    print(f"Cena: {c} zł")

print(produkty + ceny)

suma_cen = 0.0
for c in ceny:
    suma_cen += c
print(f"Ceny: {suma_cen}")

print("----------------------------------")

print(list(range(5))) # range(stop) -> liczby od 0 do stop, ALE bez stopu

print(list(range(10)))

print(list(range(2)))

for i in range(6):
    print(f"{i} HELOU :D")

print("--------------------------")
produkty = ["mysz", "płatki", "chleb", "zmywarka", "kebab"]
ceny = [249.00, 7.50, 3.49, 1699.99, 10.25]

# n - długość listy
# indeksy listy: 0, 1, 2, ..., n-1
# range(n):      0, 1, 2, ..., n-1

n = len(produkty) # 5
for i in range(n): # range(5): 0, 1, 2, 3, 4 -> PRZECHOWYWANE W ZMIENNEJ i
    print(f"Indeks {i}")
    print(f"{produkty[i]} - cena {ceny[i]} zł")


# -------- ZADANIE SAMODZIELNE ---------

wyrazy = ["drydry", "rzapka", "szponcic", "sokowirówka", "kebs", "karaiby"]
# a) Proszę napisać pętlę for na podstawie poprzednich zadań, tak aby
# ta pętla wypisała kolejne indeksy elementów listy oraz ich treść

# Indeks 0 - drydry
# Indeks 1 - rzapka
# ...
# Indeks 5 - karaiby

# b) Do wypisywanych linijek proszę dodać informację o długości wyrazu
# - proszę użyć funkcji len()