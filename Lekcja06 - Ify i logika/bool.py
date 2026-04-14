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
# Przeciwny: <

# Mniejsze lub równe
wyr = 5 <= 3 # Fałsz
wyr = 5 <= 5 # Prawda
wyr = 5 <= 8 # Prawda
# Przeciwny: >

# Mniejsze
wyr = 5 < 3 # Fałsz
wyr = 5 < 5 # Fałsz
wyr = 5 < 8 # Prawda
# Przeciwny: >=

# Większe
wyr = 5 > 3 # Prawda
wyr = 5 > 5 # Fałsz
wyr = 5 > 8 # Fałsz
# Przeciwny: <=

# Różne
wyr = 5 != 3 # Prawda
wyr = 5 != 5 # Fałsz
wyr = 5 != 8 # Prawda
# Przeciwny: ==

# Równe
wyr = 5 == 3 # Fałsz
wyr = 5 == 5 # Prawda
wyr = 5 == 8 # Fałsz
# Przeciwny: !=

# Zadanie samodzielne: (++) napisać przy każdym wyrażeniu czy jest Prawdziwe czy Fałszywe
# Z gwiazdką (+): Do każdego operatora dopasować PRZECIWNY