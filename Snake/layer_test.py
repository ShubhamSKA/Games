from turtle import Turtle, Screen

a = Turtle(shape="square")
a.color("red")
a.width(6)
b = Turtle(shape="circle")
b.color("green")
b.width(3)

b.goto(-300, 0)
b.dot()
a.goto(-300, 0)
a.dot()

a.goto(300, 0)
b.goto(300, 0)

screen = Screen()
screen.exitonclick()