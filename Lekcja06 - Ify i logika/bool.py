czy_pada = False
czy_chmury = True
czy_sloneczko = False
czy_wieje = False

print(f"Czy pada: {czy_pada}")

wiek = int(input("Ile masz lat: "))

czy_pelnoletni = wiek >= 18 # wyrażenie logiczne

if czy_pelnoletni:
    print("Pełnoletni")

if wiek >= 18:
    print("Pełnoletni")

print("--------------------------")

# Większe lub równe
wyr = 5 >= 3 # Prawda
wyr = 5 >= 5 # Prawda
wyr = 5 >= 8 # Fałsz

# Mniejsze lub równe
wyr = 5 <= 3
wyr = 5 <= 5
wyr = 5 <= 8

# Mniejsze
wyr = 5 < 3
wyr = 5 < 5
wyr = 5 < 8

# Większe
wyr = 5 > 3
wyr = 5 > 5
wyr = 5 > 8

# Różne
wyr = 5 != 3
wyr = 5 != 5
wyr = 5 != 8

# Równe
wyr = 5 == 3
wyr = 5 == 5
wyr = 5 == 8

# Zadanie samodzielne: (++) napisać przy każdym wyrażeniu czy jest Prawdziwe czy Fałszywe
# Z gwiazdką (+): Do każdego operatora dopasować PRZECIWNY