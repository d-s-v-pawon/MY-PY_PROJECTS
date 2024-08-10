import turtle
pen=turtle.Turtle()
pen.speed(0)
def curve():
    for _ in range(200):
        pen.right(1)
        pen.forward(1)
def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(125)
    curve()
    pen.forward(120)
    pen.end_fill()
def txt():
    pen.up()
    pen.setpos(-200,-200)
    pen.down()
    pen.color('red')
    pen.write("THE RELATIONSHIP BETWEEN THE TWO PERSONS IS LOVE", font=("Verdana", 12, "bold"))
heart()
txt()
pen.hideturtle()
turtle.done()
