import turtle

turtle.speed(5)

def kwadrat():
    for i in range(4):
        turtle.forward(200)
        turtle.left(90)

turtle.color('black')
for i in range(4):
    kwadrat()
    turtle.left(90)


turtle.up() # podnosi żółwia i nie zostawia już śladu

turtle.pensize(5)
turtle.color('red') # czerwony
turtle.dot()

turtle.color('blue') # niebieski
turtle.goto(-100, -100)
turtle.dot()

turtle.color('purple') # fioletowy
turtle.goto(100, 100)
turtle.dot()

turtle.color('green') # zielony
turtle.goto(100, -100)
turtle.dot()

turtle.color('yellow') # żółty
turtle.goto(-100, 100)
turtle.dot()

turtle.exitonclick()

