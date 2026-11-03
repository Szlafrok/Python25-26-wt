# Proszę napisać funkcję, która przyjmuje jako argumenty Wasze imię, nazwisko
# oraz ulubiony typ kostki brukowej. Jeżeli użytkownik nie poda arugmentu do
# kostki brukowej, należy przyjąć wartość domyślną "chodnikowa". Funkcja powinna
# wypisać przedstawienie się:

# PRZYKŁAD
# Cześć, jestem Piotrek Polański
# Mój ulubiony typ kostki brukowej to chodnikowa.

# Następnie proszę wywołać tę funkcję.

# [*] Proszę uzupełnić tę funkcję o type hinting (wyszukać co to jest) oraz
# napisać w komentarzu do czego ten type hinting służy.


### Zadanie bazowe: + + +
### Zadanie z gwiazdką: + +

def przedstaw_sie(imie, nazwisko, kostka = "chodnikowa"):
    print(f"Cześć, jestem {imie} {nazwisko} a mój ulubiony typ kostki brukowej to {kostka}")

przedstaw_sie("Piotrek", "Polański", "kocie łby")