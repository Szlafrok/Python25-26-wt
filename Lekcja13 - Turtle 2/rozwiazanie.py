from turtle import *

setup(300, 300)

#goto(0, 0)
shape("arrow")
left(135)
stamp()

goto(-100, 0)
right(90)
shape("turtle")
stamp()

goto(-100, 100)
right(90)
shape("square")
stamp()

goto(0, 100)
right(90)
shape("triangle")
stamp()

goto(0, 0)
hideturtle()

done()