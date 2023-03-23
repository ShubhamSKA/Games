from turtle import *
from time import *
from msvcrt import *
from random import *
from os import *

def food_gen():
    food.penup()
    x=(randint((-200/5),(200/5)))*5
    y=(randint((-120/5),(130/5)))*5
    food.setpos(x,y)
    food.dot(5,"orange")
    return(x,y)
    
def direction_change(dir):
    head.speed(0)
    if dir=='w':
        head.setheading(90)
    if dir=='a':
        head.setheading(180)
    if dir=='s':
        head.setheading(270)
    if dir=='d':
        head.setheading(0)
    head.speed(velocity)

def getcolor(x,y):
    y=-y
    canvas=getcanvas()
    ids=canvas.find_overlapping(x,y,x,y)
    colorsunder=[]
    if ids and len(ids)>=2:
        #for i in range(len(ids)):
            #colorsunder.append(canvas.itemcget(ids[i],"fill"))
        #print(colorsunder)
        #print(ids[0],ids[1])
        if len(ids)==3:
            if canvas.itemcget(ids[2],"fill")=='green':
                return('green')
        if canvas.itemcget(ids[0],"fill")=='black':
            return('black')
        if canvas.itemcget(ids[0],"fill")=='orange':
            return('orange')
    return('nocolor')

def point_update(point):
    points.goto(-205,138)
    points.clear()
    points.write(str(point))

def advance(length):
    direction=head.heading()
    position=head.position()
    if len(tails)<length:
        tail = head.clone()
        tails.append(tail)
        tails[-1].speed(0)
        tails[-1].pendown()
        head.forward(5)
        tails[-1].setposition(head.position())
    else:
        tails[0].undo()
        tails[0]=head.clone()
        sub=tails[0]
        del tails[0]
        tails.append(sub)
        tails[-1].speed(0)
        tails[-1].pendown()
        head.forward(5)
        tails[-1].setposition(head.position())
        



tails=[]

game=0
direction='d'
user_direction=0
invalid={b'w':b's',b'a':b'd',b's':b'w',b'd':b'a'}
total=0
length=10
velocity=11

setup(450,340)
head=Turtle()
food=Turtle()
draw=Turtle()
points=Turtle()

head.width(5)

food.ht()
head.ht()
ht()
draw.ht()
points.ht()

head.pencolor("green")

head.speed(velocity)
food.speed(0)
draw.speed(0)
points.speed(0)

points.penup()
point_update(total)
draw.penup()
draw.goto(-205,135)
draw.pendown()
draw.goto(205,135)
draw.goto(205,-125)
draw.goto(-205,-125)
draw.goto(-205,135)

head.penup()
head.goto(-150,0)
while head.xcor()<-100:
    advance(length)

food_coor=food_gen()
food_x=food_coor[0]
food_y=food_coor[1]

while game!="start":
    start=input("Should the game start (Y/N)?").lower()
    if start=='y':
        game='start'

while game!="end":
    if head.xcor()>=204 or head.xcor()<-204 or head.ycor()>=134 or head.ycor()<=-124:
        game='end'

    if kbhit():
        ui=getch()
        if ui in [b'w',b'a',b's',b'd'] and ui!=user_direction and user_direction!=invalid[ui]:
            user_direction=ui
            defined_direction=list(str(user_direction))[2]
            direction_change(defined_direction)   
 
    advance(length)

    if int(head.xcor())==food_x and int(head.ycor())==food_y or getcolor(head.xcor(),head.ycor())=='orange':
        food.clear()
        length+=1
        food_coor=food_gen()
        food_x=food_coor[0]
        food_y=food_coor[1]
        total+=4
        point_update(total)
    color_under=getcolor(head.xcor(),head.ycor())
    if color_under=='green':
        game='end'
    if color_under=='black':
        game='end'
screen=Screen()
screen.exitonclick()