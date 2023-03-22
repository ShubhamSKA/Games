from turtle import *
from time import *
from msvcrt import *
from random import *
from os import *

def food_gen():
    food.penup()
    x=(randint((-205/5),(205/5)))*5
    y=(randint((-125/5),(135/5)))*5
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
    head.speed(1)

def getcolor(x,y):
    y=-y
    canvas=getcanvas()
    ids=canvas.find_overlapping(x,y,x,y)
    colorsunder=[]
    if ids and len(ids)>=2:
        for i in range(len(ids)):
            colorsunder.append(canvas.itemcget(ids[i],"fill"))
        print(colorsunder)
        #print(ids[0],ids[1])
        if canvas.itemcget(ids[1],"fill")=='red':
            return('red')
    return('nocolor')


game=0
direction='d'
user_direction=0
invalid={b'w':b's',b'a':b'd',b's':b'w',b'd':b'a'}
loc_ind=0
loc_ind_n=9

setup(450,300)
head=Turtle()
food=Turtle()
neck=Turtle()

width(5)
head.width(5)
neck.width(5)

food.ht()
head.ht()
ht()
neck.ht()

pencolor("white")
head.pencolor("green")
neck.pencolor("red")

neck.speed(1)
speed(1)
head.speed(1)
food.speed(0)

head.penup()
head.goto(-150,0)
neck.penup()
neck.goto(-150,0)
neck.pendown()
head.pendown()
coordinates=[]
while head.xcor()<-100:
    head.forward(5)
    coordinates.append((head.xcor(),head.ycor()))
neck.goto(-105,0)
penup()
goto(-150,0)
pendown()

food_coor=food_gen()
food_x=food_coor[0]
food_y=food_coor[1]

while game!="start":
    start=input("Should the game start (Y/N)?").lower()
    if start=='y':
        game='start'

while game!="end":
    if head.xcor()>=205 or head.xcor()<-205 or head.ycor()>=135 or head.ycor()<=-125:
        game='end'

    if kbhit():
        ui=getch()
        if ui in [b'w',b'a',b's',b'd'] and ui!=user_direction and user_direction!=invalid[ui]:
            user_direction=ui
            defined_direction=list(str(user_direction))[2]
            direction_change(defined_direction)   
 
    head.forward(5)
    coordinates.append((head.xcor(),head.ycor()))
    neck.goto(coordinates[loc_ind_n][0],coordinates[loc_ind_n][1])
    goto(coordinates[loc_ind][0],coordinates[loc_ind][1])

    loc_ind+=1
    loc_ind_n+=1

    if int(head.xcor())==food_x and int(head.ycor())==food_y:
        food.clear()
        loc_ind-=3
        food_coor=food_gen()
        food_x=food_coor[0]
        food_y=food_coor[1]
    color_under=getcolor(head.xcor(),head.ycor())
    if color_under=='red':
        game='end'
done()
