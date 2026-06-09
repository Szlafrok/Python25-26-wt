import turtle as t

def oblicz_kat(n):
    return 360 / n

def wielokat(n):
    t.down()

    for i in range(n):
        t.forward(100)
        t.left(oblicz_kat(n))
    t.up()


wielokat(9)
t.done()