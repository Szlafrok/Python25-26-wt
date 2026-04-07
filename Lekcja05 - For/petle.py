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