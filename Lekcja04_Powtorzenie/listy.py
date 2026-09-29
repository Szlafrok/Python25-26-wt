zakupy = ["Mleko", "Ziemniaki", "Czekolada", "Jabłka", "Comber z żubra"]
ceny = [
    20, # int
    0.5, # float
    15, # int
    500000000, # int
    "dużo :D"
]

print(zakupy)
print(ceny)

#[20, 0.5, 15, 500000000]

print(zakupy[0]) # INDEKSUJEMY OD 0
print(zakupy[2])
print(zakupy[4])
# print(zakupy[5]) poza zakresem listy!

print(zakupy[-1]) # element ostatni - comber z żubra
print(zakupy[-2]) # jabłka
print(zakupy[-5])
# print(zakupy[-6]) # błąd

print(f"{zakupy[0]} kosztuje {ceny[0]}")