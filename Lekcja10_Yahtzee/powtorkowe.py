from random import randint

# randint(a, b) -> zwraca losową liczbę całkowitą od a do b, WŁĄCZNIE z a i b
# randint -> random integer -> losowa liczba całkowita

x = randint(1, 1000)

while True:
    liczba = int(input("Podaj liczbę: "))

    if x == liczba:
        print("Gratulacje, zgadłeś!")
        break
    elif x < liczba:
        print("Za dużo!")
    else:
        print("Za mało!")
