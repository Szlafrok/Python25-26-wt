


# Proszę utworzyć listę zawierającą imiona uczestników zajęć.
# Jedno imię w tej liście powinno być dodatkowe i się zgadzać.

# Proszę usunąć to imię z tej listy poleceniem .remove() oraz
# dodać imię trenera za pomocą polecenia .append()

# Proszę podać w komentarzu indeks, na którym znajdowało się
# błędne imię.

imiona = ["Stefan", "Wojtek", "Ula", "Ryszard", "Julka", "Maks", "Beniamin", "Antek"]

# Ryszard leży na indeksie 3
imiona.remove("Ryszard")
imiona.append("Piotr")

print(imiona)

print(f"Długość listy imiona: {len(imiona)}")

imiona.append("Józwa")

print(f"Długość listy imiona: {len(imiona)}")


tekst = "abrakadabra"
print(tekst[0]) # a
print(tekst[1]) # b
print(tekst[2]) # r
print(tekst[3]) # r

print(len(tekst))

liczby = [5, 7, 9, 10]
print(liczby[1]) # 7
print(liczby[1] * liczby[3]) # 70
#print(liczby[4] * liczby[3]) # BŁĄD


cyfry = 123

cyfry = str(123)
print(cyfry[2])