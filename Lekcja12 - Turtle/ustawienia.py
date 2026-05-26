import turtle

# kolor pisaka
turtle.pencolor('red')
turtle.pencolor("#abedff")

turtle.bgcolor("#2ca7ff")

# grubość (rozmiar) pisaka
turtle.pensize(5)

# szybkość rysowania
turtle.speed(5)

for i in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.exitonclick()