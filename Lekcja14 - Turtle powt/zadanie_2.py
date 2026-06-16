import turtle as t

kolory = ["red", "blue", "green", "orange", "magenta"]
wspolrzedne = [(0, 0), (-100, -100), (-100, 100), (100, -100), (100, 100)]


def kwadrat(x, y, kolor): # zbuduje kwadrat o boku 30 i wypełni go kolorem
    t.up()
    t.goto(x, y)
    t.down()
    t.fillcolor(kolor)
    t.begin_fill()
    for i in range(4):
        t.forward(30)
        t.left(90)
    t.end_fill()

for i in range(5):

    print(wspolrzedne[i], kolory[i])

    x = wspolrzedne[i][0]
    y = wspolrzedne[i][1]
    kolor = kolory[i]

    kwadrat(x, y, kolor)