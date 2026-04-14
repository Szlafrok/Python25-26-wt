### Zadanie dodatkowe: Czuć nosem zimę (⭐)

Instrukcja `match ... case` pozwala na sprawdzanie warunków przez dopasowywanie wzorców. Umożliwia ona tworzenie instrukcji warunkowych elastyczniejsze, niż z pomocą konstrukcji `if-elif-else`.

Jak to robić?

```py
wartosc = int(input())
match wartosc:
    case 123: # Wykona się, jeśli zmienna jest równa podanej wartości
        print("Wartość jest równa 123")
    case 456:
        print("Wartość jest równa 456")
    case 0 | 1: # Wykona się, jeśli zmienna jest równa którejś z podanych wartości oddzielonych |
        print("Wartość jest równa 0 lub jest równa 1")
    case 2 | 3 | 4:
        print("Wartość jest równa 0, 1 lub 2")
    case _: # Przez _ oznaczamy "domyślną" zwracaną wartość
        print("Żaden z warunków nie został spełniony")
```

Przy tworzeniu instrukcji `match ... case` warto pamiętać, że:

1. Jeśli jakiś przypadek wartości nie zostanie rozpatrzony, nic się nie wydarzy (np. może brakować `case _` i nic się nie stanie, jeśli podamy błędną wartość)
2. Jeśli któryś przypadek `case` się wypełni, wszystkie pozostałe nie będą dalej sprawdzane, nawet jeśli również spełniłyby podane warunki.

---

Poniższa tabela przechowuje informacje o datach ferii zimowych w poszczególnych województwach.
| **Termin** | **Województwa** |
|:------------------------:|---------------------------------------------------------------------------------|
| 19 stycznia – 1 lutego 2026 | mazowieckie, pomorskie, podlaskie, świętokrzyskie, warmińsko-mazurskie |
| 2 lutego – 15 lutego 2026 | dolnośląskie, kujawsko-pomorskie, łódzkie, zachodniopomorskie, małopolskie, opolskie |
| 16 lutego – 1 marca 2026 | podkarpackie, lubelskie, wielkopolskie, lubuskie, śląskie |

Proszę napisać program, który wczyta od użytkownika nazwę jego województwa **(może być zarówno WIELKIMI, małymi, jak i MiESzaNYMi)** i wypisze mu do konsoli informację o zakresie czasowym jego ferii zimowych.

Wskazówka: zastanowienie się co zrobi poniższy program może pomóc 😉

```py
tekst = "TEksT"
print(tekst.lower())
```