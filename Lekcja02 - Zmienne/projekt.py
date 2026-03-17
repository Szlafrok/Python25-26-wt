zmienna = 5
zmienna = 7
zmienna_2 = 10

tekst = "hyhyhy ktokolwiekcokolwiekcoś"

print(zmienna_2) # wypisanie wartości zmiennej

tekst_1 = "abc"
tekst_2 = "def"

polaczone = tekst_1 + tekst_2

print(polaczone)

liczba_1 = 12
liczba_2 = 12

suma = liczba_1 + liczba_2

print(suma)

# print(tekst_1 + liczba_1) BŁAD

# -------------------------------

typ_1 = 12 # liczba całkowita -> int (integer)
typ_2 = "abc" # tekst (ciąg znaków) -> str (string)
typ_3 = 13.5 # liczba zmiennoprzecinkowa -> float
typ_4 = True # typ logiczny prawda/fałsz -> bool

print(type(typ_1))
print(type(typ_2))
print(type(typ_3))
print(type(typ_4))

# int()
# str()

wiek = 50
tekst = "Mój wiek wynosi "

wiek = str(wiek)

print(tekst + wiek)

tekst_1 = "10"
tekst_2 = "stonks internet u mnie wrócił lubię jeść jeść jeść lubię jeść banany bananynany"

liczba_1 = int(tekst_1)
#liczba_2 = int(tekst_2) BŁĄD!

imie = input("Jak masz na imię? ")
print(imie)

wiek = int(input("Ile masz lat? "))
print(wiek)
print(wiek + 1)

# Proszę za pomocą funkcji input wczytać od użytkownika imię i
# zapisać je do zmiennej. Proszę następnie wczytać jego wiek jako
# LICZBĘ CAŁKOWITĄ (int) i również zapisać go do zmiennej.

# Następnie na bazie informacji z czata GPT, proszę zapisać
# w jednym zdaniu: "Hej, jestem {imię} i za rok będę mieć {wiek + 1} lat."
# Proszę użyć f-stringa.

imie = input("Jak się nazywasz? ")
wiek = int(input("Ile masz lat? "))

print(f"Jestem {imie} i za rok będę miała {wiek + 1} lat")