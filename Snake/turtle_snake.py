from turtle import *
from time import *
from msvcrt import *
from random import *
from os import *

def advance():
    head.pendown()
    head.forward(5)

def food_gen():
    food.penup()
    x=(randint((-435/5),(435/5)))*5
    y=(randint((-285/5),(285/5)))*5
    food.setpos(x,y)
    food.dot(5,"orange")
    return(x,y)
    
def direction_change(dir):
    speed("fastest")
    if dir=='w':
        head.setheading(90)
    if dir=='a':
        head.setheading(180)
    if dir=='s':
        head.setheading(270)
    if dir=='d':
        head.setheading(0)
    speed(1)

def getcolor(x,y):
    y=-y
    canvas=getcanvas()
    ids=canvas.find_overlapping(x,y,x,y)
    if ids and len(ids)>3:
        allcolors=
        index=ids[-3]
        for i in range(len(ids)):
            index=ids[i]
            colorunder=canvas.itemcget(index,"fill")
        
        if colorunder:
            return colorunder
    if ids and len(ids)>1:
        print(len(ids))
        index=ids[-2]
        colorunder=canvas.itemcget(index,"fill")
        if colorunder:
            return colorunder
    return "nocolor"

game=0
direction='d'
user_direction=0
invalid={b'w':b's',b'a':b'd',b's':b'w',b'd':b'a'}
loc_ind=0

setup(900,600)
speed(1)
width(5)
head=Turtle()
head.width(5)
food=Turtle()
food.ht()
head.ht()
ht()

pencolor("white")
head.pencolor("green")
head.penup()
head.goto(-150,0)
coordinates=[]
while head.xcor()<-100:
    advance()
    coordinates.append((head.xcor(),head.ycor()))
penup()
goto(-150,0)
pendown()
food_coor=food_gen()
food_x=food_coor[0]
food_y=food_coor[1]

while game!="start":
    #system('cls')
    start=input("Should the game start (Y/N)?").lower()
    if start=='y':
        game='start'

while game!="end":
    if head.xcor()>=435 or head.xcor()<=-435 or head.ycor()>=290 or head.ycor()<=-290:
        game='end'
    if kbhit():
        ui=getch()
        if ui in [b'w',b'a',b's',b'd'] and ui!=user_direction and user_direction!=invalid[ui]:
            user_direction=ui
            defined_direction=list(str(user_direction))[2]
            direction_change(defined_direction)    
    advance()
    #print(int(head.xcor()),int(head.ycor()))
    if int(head.xcor())==food_x and int(head.ycor())==food_y:
        food_coor=food_gen()
        food_x=food_coor[0]
        food_y=food_coor[1]
    coordinates.append((head.xcor(),head.ycor()))
    goto(coordinates[loc_ind][0],coordinates[loc_ind][1])
    loc_ind+=1
    print(getcolor(head.xcor(),head.ycor()))
    
done()
