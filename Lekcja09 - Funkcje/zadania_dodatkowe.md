# Zadania dodatkowe ⭐

### Zadania pokazujemy przed zajęciami lub tuż po zajęciach!

Aby zdobyć bonusy, potrzebujemy:

| Nagroda | Minimalny wynik |
| ------- | --------------- |
| ⭐ | 4 pkt |
| ⭐➕ | 5 pkt |
| ⭐➕➕ | 6 pkt |
| ⭐➕➕➕ | 9 pkt |
| 🎁❓ | 15 pkt |

---

## Zadania Łatwiejsze 🎯

### Zadanie 1 `2 pkt`
Napisz funkcję `predkosc(droga, czas)`, która przyjmuje jako argumenty:
- `droga`: dystans przebyty przez podróżnika w kilometrach (km)
- `czas`: czas podróży w godzinach (h)
i **ZWRACA** (nie printuje, zwraca!) średnią prędkość podróżnika w km/h.

### Zadanie 2 `2 pkt`
Napisz funkcję `pole_trapezu(a, b, h)`, która przyjmuje jako argumenty:
- `a`: podstawę dolną trapezu
- `b`: podstawę górną trapezu
- `h`: wysokość trapezu
i **ZWRACA** (nie printuje, zwraca!) pole trapezu wyrażone wzorem (a+b)*h / 2

### Zadanie 3 `2 pkt` (lub więcej)
Popisz się


Beniamin 10 / 6
---

## Zadania Trudniejsze 🏆
[🤖] Można wspomóc się sztuczną inteligencją... ale należy umieć wyjaśnić swoje rozwiązanie!

### Zadanie 1 `4 pkt`

Ciąg arytmetyczny to taki ciąg liczb, że pomiędzy dwoma sąsiednimi elementami jest zawsze taka sama różnica. Przykładowo:

- Ciąg `[2, 4, 6, 8, 10]` jest ciągiem arytmetycznym.
- Ciąg `[2, 6, 4, 8, 10]` NIE jest ciągiem arytmetycznym.

Proszę napisać funkcję arytm(ciag), która przyjmuje jako argument listę liczb całkowitych i zwraca:
- True, jeżeli ciąg jest arytmetyczny
- False, jeżeli ciąg nie jest arytmetyczny.

**Przykład:** Dla podanych wywołań otrzymamy:

`arytm([-1, 5, 11, 17, 23])` -> `True` (różnica == 6)

`arytm([5, 4, 3, 2, 1])` -> `True` (różnica == -1)

`arytm([5, 5, 5, 5])` -> `True` (różnica == 0)

`arytm([7, 8, 7, 6])` -> `False` (różnica nie jest stała)

Szablon:

```py
def arytm(ciag):
    pass
```

Uwaga: ciąg musi zawierać przynajmniej JEDEN element!

### Zadanie 2 `4 pkt`
Proszę napisać funkcję, która przyjmuje jako argument liczbę naturalną n i zwraca:
- `True`, jeżeli liczba jest pierwsza
- `False`, w przeciwnym razie.

Szablon:

```py
def is_prime(n):
    pass
```
### SPRAWDZARKA 📊

```py
# Ten program pomoże Ci przetestować poprawność Twojego rozwiązania - możesz sprawnie wprowadzić dane i sprawdzić, jak zachowa się Twój program.
def check(zad):
    if zad == 1:
        x = []
        print("Wpisz 'stop', aby przerwać wpisywanie liczb.")
        odp = ""
        while True:
            odp = input("Wprowadź element ciągu: ")
            if odp == "stop": 
                break
            x.append(int(odp))
        print("Ciąg jest arytmetyczny" if arytm(x) else "Ciąg nie jest arytmetyczny")
    else:
        x = int(input("Podaj liczbę: "))
        print("Liczba jest pierwsza" if is_prime(x) else "Liczba nie jest pierwsza")

check(2) # Wprowadź numer zadania i uruchom program, aby przetestować swoje rozwiązanie.
```

### Zadanie 3 `2 pkt`
Proszę opatrzyć sprawdzarkę komentarzami wyjaśniającymi jej działanie lub omówić trenerowi działanie sprawdzarki na koniec lekcji.



AquaQ ++