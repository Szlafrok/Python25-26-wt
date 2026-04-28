lista = [1, 2, 5, 4, 3, 3]

print(sum(lista))

print(min(lista))
print(max(lista))

print(lista.count(3))


tekst = "umpalumpas"

for litera in tekst:
    print("--" + litera + "--") # dodawanie stringów - KONKATENACJA

x = 4
if x > 3: # zagnieżdżenie
    print("większy od 3")
    if x % 2 == 0:
        print("parzysty")


# hasla = {"abc": 1234, "def": 4567}
# print(hasla["def"])