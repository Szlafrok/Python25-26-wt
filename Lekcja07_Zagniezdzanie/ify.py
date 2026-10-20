wiek = int(input("Podaj wiek: "))

prawko = input("Czy masz prawko (tak/nie)")

if prawko == "tak":
    czy_prawo = True
else:
    czy_prawo = False

czy_prawo = prawko == "tak"

if wiek >= 18 and czy_prawo:
    print("OK")
else:
    print("Komunikacja miejska kolego")

# Proszę napisać instrukcję if / else, która sprawdza,
# czy użytkownik ma prawo jazdy (wpisał "tak") i wpisać
# do zmiennej czy_prawo wartość True lub False. (+++)

# Bonus (++) proszę to zrobić w 1 linijce

if wiek < 10:
    print("Kolego nie dosięgniesz do kierownicy!")
elif wiek < 18:
    print("Niedługo będziesz mógł jeździć tirem!")
else:
    print("Baw się dobrze :D")

# if warunek:
#     jedna akcja
# else:
#     druga akcja
#



# ZADANIE Z GWIAZDKĄ (++)
# Proszę omówić różnicę pomiędzy podejściem z if / else, a z if / if not