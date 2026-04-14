hp = float(input("Podaj HP: "))

if hp < 0:
    print("YOU DED! :C")

print("heheszki")

if hp > 0:
    print("ŻYJEMY! :D")

# ZADANIE SAMODZIELNE

# Proszę wczytać od użytkownika do zmiennej jego prędkość (typ danych INT)
# Następnie, jeśli jedzie on ponad 140 km/h, proszę powiedzieć mu że jedzie
# za szybko, a jeśli jedzie mniej niż 30 km/h, proszę powiedzieć mu, że jedzie
# za wolno.

predkosc = int(input("Podaj prędkość w km/h: "))
if predkosc > 140:
    print("PRRRRRRRRRRR ZWOLNIJ")
if predkosc < 30:
    print("GAZ DO DECHY, LEWY PAS TO NIE KÓŁKO RÓŻAŃCOWE")