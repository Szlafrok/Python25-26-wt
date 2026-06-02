import turtle

turtle.pencolor("#009dff") # kolor pisaka
turtle.pensize(3) # rozmiar pisaka
turtle.fillcolor("#7374C1") # kolor wypełnienia

turtle.begin_fill()

for i in range(4): # część KOLOROWANA
    turtle.forward(100)
    turtle.left(45)
turtle.end_fill()

for i in range(4): # część BEZ KOLOROWANIA
    turtle.forward(100)
    turtle.left(45)

turtle.done()