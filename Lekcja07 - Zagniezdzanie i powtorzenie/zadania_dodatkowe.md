# Zadania dodatkowe ⭐

### Zadania pokazujemy przed zajęciami lub tuż po zajęciach!

Aby zdobyć bonusy, potrzebujemy:

| Nagroda | Minimalny wynik |
| ------- | --------------- |
| ⭐ | 4 pkt |
| ⭐➕ | 6 pkt |
| ⭐➕➕ | 8 pkt |
| 🎁❓ | 15 pkt |
---

Przygotowałem prostszy zestaw kilku zadań, oraz trudniejszy zestaw dwóch. Do wyboru!

---

### Zadania Łatwiejsze 🎯
Dwa z czterech zadań wykonane poprawnie dają gwiazdkę!

#### Zadanie 1 (2 pkt)
Zapisz do zmiennej wiek użytkownika jako liczbę całkowitą (`int`). Do drugiej zmiennej proszę zapisać wartość logiczną `True/False`, która określa, czy ma zgodę rodzica. Nie trzeba korzystać z `input()`, można podać gotowe wartości.

Następnie proszę napisać instrukcję warunkową `if-else`, która sprawdza czy użytkownik ma co najmniej 18 lat **lub** ma zgodę rodzica. Użytkownik powinien dostać informację, czy może zapisać się na wycieczkę, czy nie.

### Zadanie 2 (2 pkt)
Napisz program, który wczytuje od użytkownika jego liczbę plusów i za pomocą instrukcji `if/elif/else` informuje go, czy zdobył dwie gwiazdki (10+ plusów), jedną (5-9 plusów) czy zero (poniżej 5 plusów)

### Zadanie 3 (2 pkt)
Za pomocą funkcji `random.randint` lub `random.randrange` napisz program, który wylosuje dowolną liczbę dwucyfrową podzielną przez 5 - może wylosować 10, 15, 20, ..., 90, 95.

Rozpocznij w ten sposób:
```py
import random
losowa = # miejsce na Twój kod!
```

### Zadanie 4 (2 pkt)
Napisz program, który wczytuje jakiś tekst i za pomocą metody `.islower()` liczy, ile w tekście jest małych liter.

Funkcja `.islower()` zwraca `True` jeśli dana litera (lub tekst) składa się wyłącznie z małych liter, np.
```py
"abc".islower() # True
"ABc".islower() # False
"a".islower() # True
```

Można wspomóc się sztuczną inteligencją, ale trzeba wówczas być gotowym na opowiedzenie o swoim kodzie przy oddawaniu zadania!


### Zadania Trudniejsze 🏆
Jedno z dwóch zadań wykonane poprawnie daje gwiazdkę!

#### Zadanie 1 (5 pkt)
Wczytaj od użytkownika hasło. Następnie należy sprawdzić:
- czy to hasło ma od 8 do 20 znaków
- czy zawiera co najmniej jedną literę wielką
- czy zawiera co najmniej jedną cyfrę
- czy zawiera co najmniej jeden znak specjalny (który nie jest literą, wielką literą ani małą literą)

Program powinien wypisać informację, czy to hasło spełnia wymagania. Dodatkowy punkt można zdobyć za uporządkowany i czytelny kod opatrzony komentarzami!

Przydatne funkcje: `.isupper()`, `.islower()`, `.isdigit()`, `len()`

#### Zadanie 2 (5 pkt)
Dana jest lista `T`, która zawiera `N` liczb naturalnych. Proszę napisać program, który policzy i wypisze, ile jest takich liczb w tej tablicy, które są większe od liczby na poprzedniej pozycji.

Przykład: W liście `[1, 5, 6, 3, 4, 2]` są 3 takie liczby: 5 (bo jest większe od 1), 6 (bo jest większe od 5) oraz 4 (bo jest większe od 3).

Szablon rozwiązania:
```py
T = [4, 6, 5, 7, 8, 6, 5, 7, 4, 1, 0, 4, 5, 6, 9]
N = len(T)

# Miejsce na Twoje rozwiązanie
```