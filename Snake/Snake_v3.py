from turtle import *
from msvcrt import kbhit,getch
from random import randint
from math import ceil
from time import sleep

#Function that defines where the food will appear, and draws it
def food_gen():
    screen=Screen()
    screen.tracer(False)

    food.penup()
    x=(randint((-200/advancement),(200/advancement)))*advancement
    y=(randint((-120/advancement),(130/advancement)))*advancement
    food.setpos(x,y)
    food.dot(5,"orange")

    screen.tracer(True)
    return(x,y)
#Function that readjusts the direction of the head turtle, allowing the snake to turn    
def direction_change(dir):
    screen=Screen()
    screen.tracer(False)

    if dir=='w':
        head.setheading(90)
    if dir=='a':
        head.setheading(180)
    if dir=='s':
        head.setheading(270)
    if dir=='d':
        head.setheading(0)

    screen.tracer(True)
    head.speed(velocity)
#Function that returns the relevant color at the coordinate, if the color is green, black or orange
def getcolor(x,y):
    y=-y #correcting for the change in coordinate system that will occur
    canvas=getcanvas()
    ids=canvas.find_overlapping(x,y,x,y) #locates the colors within the rectangle
    
    if ids and len(ids)>=2:
        if len(ids)==3:
            if canvas.itemcget(ids[2],"fill")=='green':
                return('green')
        if canvas.itemcget(ids[0],"fill")=='black':
            return('black')
        if canvas.itemcget(ids[0],"fill")=='orange':
            return('orange') #returns the color, when relevant

    return('nocolor')
#Function to update the point total on screen
def point_update(point):
    points.goto(-205,138)
    points.clear()
    points.write(str(point))
#Function to advance the snake
def advance(length):
    screen=Screen()

    direction=head.heading()
    position=head.position()

    if len(tails)<length: #To allow the snake to reach it's expected length
        tail = head.clone() #create a clone
        tails.append(tail) #append to the array of visible turtles
        tails[-1].speed(0) #set speed of movement of most recent clone
        tails[-1].pendown()
        screen.tracer(False)
        head.forward(advancement)
        screen.tracer(True)
        tails[-1].setposition(head.position()) #make this clone follow the head

    else:
        tails[0].undo() #remove the trace of the last turtle in the array
        tails.append(tails.pop(0)) #move the last turtle in the tail to the end of the array
        tails[-1].penup() 
        screen.tracer(False)
        tails[-1].goto(position)
        tails[-1].setheading(direction) #move the turtle to the position of the head
        screen.tracer(True)
        tails[-1].speed(0)
        tails[-1].pendown()
        screen.tracer(False)
        head.forward(advancement) #advance the head turtle
        screen.tracer(True)
        tails[-1].setposition(head.position()) #move the traceing turtle to the point to where the head is
#Function to set up the board and the snake        
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
    draw.goto(-205,135) #create the borders

    head.penup()
    head.goto(-150,0)
    while head.xcor()<-100:
        advance(length)
#Function to animate the ending
def endgame(point):
    deco=Turtle()
    deco.ht()

    #list of acceptable colors
    colores=['deep pink','red','chartreuse','blue violet','magenta','spring green','blue','deep sky blue','pale green','medium violet red','violet','yellow','cyan','medium spring green','medium orchid']
    
    #animate dots
    for i in range(point):
        deco.penup()
        deco.speed(0)
        x=(randint((-200/advancement),(200/advancement)))*advancement
        y=(randint((-120/advancement),(130/advancement)))*advancement
        colour= i % len(colores)
        deco.setpos(x,y)
        deco.dot(5,colores[colour])
    
    #animate the points
    points.color('green')
    x=-1*len(str(point))/2.0*(100/3.0)
    points.goto(x,-25)
    points.write(point, font=('Impact', 45, 'normal'))

    #animate the fireworks
    for i in range(int(point/4)):
        x=(randint((-200/advancement),(200/advancement)))*advancement
        y=(randint((-120/advancement),(130/advancement)))*advancement
        firework(x,y)
#Function to animate a fireworks
def firework(x,y):
    screen=Screen()

    screen.colormode(255)
    fire=Turtle()
    fire.ht()
    fire.speed(0)

    #list of colors in rgb
    colores=[(255,20,147),(255,0,0),(127,255,0),(138,43,226),(255,0,255),(0,255,127),(0,0,255),(0,191,255),(152,251,152),(199,21,133),(238,130,238),(255,255,0),(0,255,255),(0,250,154),(186,85,211)]
    colour=colores[randint(0,len(colores)-1)] #define the color of the firework
    fire.penup()
    fire.goto(x,y)

    n=randint(4,16) #define the number of points it will form
    corners=[]
    for i in range(n):
        branch=fire.clone()
        branch.setheading(360*i/n)
        branch.forward(10)
        corners.append(branch) #creating a list of turtles that will represent each of the "trails"

    screen.tracer(2)
    while colour!=(255,255,255): 
        for i in range(n):
            corners[i].clear()
            corners[i].forward(5)
            corners[i].dot(5,colour)
        colour=colorupdate(colour)
        sleep(0.01) #move forward down the trail, towards white

#Function to fade a color
def colorupdate(colour):
    r=colour[0]
    g=colour[1]
    b=colour[2]

    rp=255-r
    gp=255-g
    bp=255-b #differencce from necessary value for white

    rp=int(ceil(rp/10))
    gp=int(ceil(gp/10))
    bp=int(ceil(bp/10)) #advancement towards white

    r+=rp
    g+=gp
    b+=bp #advance the color

    return(r,g,b)

## NECESSARY VARIABLES
tails=[] #list storing all the parts of the tail
game=0 #intitial value of game
direction='d' #initial value for direction
user_direction=0 #initial value for valid input direction
invalid={b'w':b's',b'a':b'd',b's':b'w',b'd':b'a'} #dictionary of invalid turns
total=0 #number of points
length=10 #length of the snake
velocity=11 #velocity of head
advancement=5 #each advancement of the snake
ui=0 #received value

setup(450,340) #initial setup
head=Turtle()
food=Turtle()
draw=Turtle()
points=Turtle() #initializing turtles

initialization()
food_coor=food_gen() #generating food

while game!="start" and game!='end':
    start=input("Should the game start (Y/N)?").lower() #ask for input start, so that the user is in the terminal
    if start=='y':
        game='start'
    elif start=='n':
        game='end' 

while game!="end":
    if head.xcor()>=204 or head.xcor()<-204 or head.ycor()>=134 or head.ycor()<=-124:
        game='end' #lose game if you leave board

    if kbhit():
        ui=getch() #recieve input
        if ui in [b'w',b'a',b's',b'd'] and ui!=user_direction and user_direction!=invalid[ui]: #check if the iser direction is valid
            user_direction=ui
            defined_direction=list(str(user_direction))[2] #assign the direction
            direction_change(defined_direction)  #change direction

    advance(length) #move snake

    color_under=getcolor(head.xcor(),head.ycor()) #check what color is underneath

    if int(head.position()==food_coor or color_under=='orange'): #check for food, and increase length if food is consumed
        food.clear()
        length+=2
        food_coor=food_gen()
        total+=4
        point_update(total)
    
    if color_under=='green' or color_under=='black': #end game
        game='end'

clearscreen()
endgame(total) #end of game animations


screen=Screen()
screen.exitonclick()