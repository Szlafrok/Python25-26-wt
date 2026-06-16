import turtle as t

t.up()

def after_click(x, y):
    print("test")

    t.goto(x, y)
    t.down()
    t.dot(10)
    t.up()

t.onscreenclick(after_click)

t.done()