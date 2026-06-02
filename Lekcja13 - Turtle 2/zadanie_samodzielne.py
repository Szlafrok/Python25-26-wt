# Korzystając z kodu z poprzednich zajęć oraz z kodu zapisanego w
# poprzednim ćwiczeniu proszę narysować trójkąt.

# Kolor wypełnienia - czerwony (red)
# Kolor obwódki - żółty (yellow)
# Grubość obwódki - 4

# Trójkąt ma być równoboczny!

import turtle

turtle.pencolor('yellow')
turtle.pensize(4)
turtle.fillcolor('red')

turtle.begin_fill()

for i in range(3):
    turtle.forward(100)
    turtle.left(120)

turtle.end_fill()
turtle.done()