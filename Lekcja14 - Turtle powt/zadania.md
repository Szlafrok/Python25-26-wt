1. Napisz funkcję zgodnie z poniższym szablonem:

```py
def wielokat(n):
    pass # miejsce na Twoją implementację!
```

Funkcja powinna rysować wielkokąt o podanej liczbie kroków. Jesli podamy tej funkcji argument n=3, dostaniemy trójkąt równoboczny. Jeśli podamy n=4, dostaniemy kwadrat, itd.

Do naszej dyspozycji jest funkcja
```py
def oblicz_kat(n):
    return 360 / n

t.left(oblicz_kat(n))
```
która liczy, o ile stopni należy się obrócić, aby narysować kolejny bok wielokąta (przykładowo, dla kwadratu za każdym bokiem obracamy się o 90 stopni)