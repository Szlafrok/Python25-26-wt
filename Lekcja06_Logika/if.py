print(5 == 4) # równość

print(7 * 8 == 56)

print(7*8 > 56) # większe - FAŁSZ

print(7*8 < 56) # mniejsze - FAŁSZ

print(7*8 != 56) # nierówne/różne - FAŁSZ

print(7*8 >= 56) # większe LUB równe - PRAWDA

print(7*8 <= 56) # mniejsze LUB równe - PRAWDA

wiek = int(input("Podaj wiek: "))

if wiek >= 18:
    print("Pełnoletni")
if not wiek >= 18:
    print("Nieletni")