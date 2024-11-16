from turtle import *
tracer(0)
screensize(1500, 1500)
c = 20
left(90)

for x in range(9):
    fd(c*29)
    rt(90)
    fd(17*c)
    rt(90)
up()
fd(c*5)
rt(90)
fd(c*1)
lt(90)
down()
for x in range(9):
    fd(c*64)
    rt(90)
    fd(48*c)
    rt(90)


up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*c, y*c)
        dot(3, "black")

update()
exitonclick()
