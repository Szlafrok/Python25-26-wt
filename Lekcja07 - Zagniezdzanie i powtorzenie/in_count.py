import random
#print(random.randint(1, 10))

lista = []

for i in range(8):
    lista.append(random.randint(1, 10))

print(lista)

print(lista.count(10))

print(7 in lista)


