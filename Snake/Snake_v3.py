from turtle import *
from msvcrt import *
from random import randint
from math import *

def food_gen():
    food.penup()
    x=(randint((-200/advancement),(200/advancement)))*advancement
    y=(randint((-120/advancement),(130/advancement)))*advancement
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
        head.forward(advancement)
        tails[-1].setposition(head.position())
    else:
        tails[0].undo()
        tails[0]=head.clone()
        sub=tails[0]
        del tails[0]
        tails.append(sub)
        tails[-1].speed(0)
        tails[-1].pendown()
        head.forward(advancement)
        tails[-1].setposition(head.position())
        
def initialization():
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

def endgame(point):
    deco=Turtle()
    deco.ht()
    colores=['deep pink','red','chartreuse','blue violet','magenta','spring green','blue','deep sky blue','pale green','medium violet red','violet','yellow','cyan','medium spring green','medium orchid']
    for i in range(point):
        deco.penup()
        deco.speed(0)
        x=(randint((-200/advancement),(200/advancement)))*advancement
        y=(randint((-120/advancement),(130/advancement)))*advancement
        colour= i % len(colores)
        deco.setpos(x,y)
        deco.dot(5,colores[colour])
    for i in range(int(point/10)):
        x=(randint((-200/advancement),(200/advancement)))*advancement
        y=(randint((-120/advancement),(130/advancement)))*advancement
        firework(x,y)
    point=str(point)
    points.color('green')
    x=-1*len(point)/2.0*(100/3.0)
    points.goto(x,-25)
    points.write(point, font=('Impact', 45, 'normal'))

def firework(x,y):
    screen=Screen()
    screen.colormode(255)
    fire=Turtle()
    fire.ht()
    fire.speed(0)
    colores=[(255,20,147),(255,0,0),(127,255,0),(138,43,226),(255,0,255),(0,255,127),(0,0,255),(0,191,255),(152,251,152),(199,21,133),(238,130,238),(255,255,0),(0,255,255),(0,250,154),(186,85,211)]
    colour=colores[randint(0,len(colores)-1)]
    fire.penup()
    fire.goto(x,y)
    n=randint(4,16)
    corners=[]
    for i in range(n):
        branch=fire.clone()
        branch.setheading(360*i/n)
        branch.forward(10)
        corners.append(branch)
    screen.tracer(3,40000)
    while colour!=(255,255,255): 
        for i in range(n):
            corners[i].clear()
            corners[i].forward(5)
            corners[i].dot(5,colour)
        colour=colorupdate(colour)
        delay(1300)

def colorupdate(colour):
    r=colour[0]
    g=colour[1]
    b=colour[2]
    rp=255-r
    gp=255-g
    bp=255-b
    rp=int(ceil(rp/10))
    gp=int(ceil(gp/10))
    bp=int(ceil(bp/10))
    r+=rp
    g+=gp
    b+=bp
    return(r,g,b)

tails=[]
game=0
direction='d'
user_direction=0
invalid={b'w':b's',b'a':b'd',b's':b'w',b'd':b'a'}
total=0
length=10
velocity=11
advancement=5
ui=0

setup(450,340)
head=Turtle()
food=Turtle()
draw=Turtle()
points=Turtle()

initialization()
food_coor=food_gen()

while game!="start":
    start=input("Should the game start (Y/N)?").lower()
    if start=='y':
        game='start'
    elif start=='n':
        game='end'

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

    color_under=getcolor(head.xcor(),head.ycor())

    if int(head.position()==food_coor or color_under=='orange'):
        food.clear()
        length+=2
        food_coor=food_gen()
        total+=4
        point_update(total)
    
    if color_under=='green' or color_under=='black':
        game='end'

clearscreen()
endgame(total)


screen=Screen()
screen.exitonclick()