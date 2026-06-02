# Zadanie samodzielne

# Proszę napisać FUNKCJE, które utworzą figury (1 figura - 1 funkcja)

# Funkcje nie mają zwracać nic, mają jedynie utworzyć zadaną figurę i
# po wykonaniu działania wypisać "OK" do konsoli za pomocą printa.

# - kwadrat
# - prostokąt
# - trójkąt równoboczny

import turtle

def kwadrat():
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    print("OK")

def prostokat():
    for i in range(2):
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(60)
        turtle.left(90)
    print("OK")

def trojkat():
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)
    print("OK")

kwadrat()
turtle.exitonclick()
