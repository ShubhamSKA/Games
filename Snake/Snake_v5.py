from turtle import *
from msvcrt import kbhit,getch
from random import randint
from math import ceil
from time import sleep, time

#Function that defines where the food will appear, and draws it
def food_gen():
    screen=Screen()
    screen.tracer(False)

    food.penup()

    x=(randint((-200/advancement),(200/advancement)))*advancement
    y=(randint((-120/advancement),(130/advancement)))*advancement
    while getcolor(x,y)=='green': #making sure the food does not appear on the snake
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
            return('orange') 
        if canvas.itemcget(ids[0],"fill")=='red':
            return('red')
        #returns the color, when relevant

    return('nocolor')
#Function to update the point total on screen
def point_update(point):
    screen=Screen()
    screen.tracer(False)
    points.goto(-205,138)
    points.clear()
    points.write(str(point))
    screen.tracer(True)
#Function to advance the snake
def advance(length,pause):
    screen=Screen()

    direction=head.heading()
    position=head.position()

    if len(tails)<length: #To allow the snake to reach it's expected length
        tail = head.clone() #create a clone
        tails.append(tail) #append to the array of visible turtles
        #tails[-1].speed(0) #set speed of movement of most recent clone
        tails[-1].pendown()
        screen.tracer(False)
        head.forward(advancement)
        tails[-1].setposition(head.position()) #make this clone follow the head
        sleep(1/pause)
        screen.update()
        screen.tracer(True)
    else:
        tails[0].undo() #remove the trace of the last turtle in the array
        tails.append(tails.pop(0)) #move the last turtle in the tail to the end of the array
        tails[-1].penup() 
        screen.tracer(False)
        tails[-1].goto(position)
        tails[-1].setheading(direction) #move the turtle to the position of the head
        tails[-1].pendown()
        head.forward(advancement) #advance the head turtle
        tails[-1].setposition(head.position()) #move the traceing turtle to the point to where the head is
        sleep(1/pause)
        screen.update()
        screen.tracer(True)
#Function to set up the board and the snake
def initialization():
    head.width(5)

    food.ht()
    head.ht()
    ht()
    draw.ht()
    points.ht()
    special.ht()
    timer.ht()

    head.pencolor("green")

    timer.shape('square')
    timer.shapesize(0.2,0.2,1)
    timer.penup()

    head.speed(velocity)
    food.speed(0)
    draw.speed(0)
    points.speed(0)
    timer.speed(0)

    screen=Screen()
    screen.tracer(False)
    points.penup()
    point_update(total)
    draw.penup()
    draw.goto(-205,135)
    draw.pendown()
    draw.goto(205,135)
    draw.goto(205,-125)
    draw.goto(-205,-125)
    draw.goto(-205,135) #create the borders
    draw.penup()
    draw.goto(-32,10)
    square(20,'A')
    draw.goto(-10,10)
    square(20, 'S')
    draw.goto(12,10)
    square(20,'D')
    draw.goto(-10,32)
    square(20,'W')
    draw.goto(-90,55)
    draw.write("Go to terminal and type Y + Enter to start")
    screen.tracer(True)
    head.penup()
    head.goto(-150,0)
    while head.xcor()<-100:
        advance(length,move_delay)
#Function to animate the ending
def endgame(point,highscore):
    deco=Turtle()
    deco.ht()
    screen=Screen()
    #list of acceptable colors
    colores=['deep pink','red','chartreuse','blue violet','magenta','spring green','blue','deep sky blue','pale green','medium violet red','violet','yellow','cyan','medium spring green','medium orchid']
    
    #animate dots
    screen.tracer(False)
    for i in range(point):
        deco.penup()
        deco.speed(0)
        x=(randint((-200/advancement),(200/advancement)))*advancement
        y=(randint((-120/advancement),(130/advancement)))*advancement
        colour= i % len(colores)
        deco.setpos(x,y)
        deco.dot(5,colores[colour])
        sleep(0.01)
        screen.update()
    screen.tracer(True)
    
    #animate the points
    points.color('green')
    points.goto(-300,-25) #establish starting point of points turtle
    x=-1*len(str(point))/2.0*(100/3.0) #establishe ending point of points turtle
    screen.tracer(False)
    while points.xcor()<x:
        points.clear()
        points.write(point, font=('Impact', 45, 'normal'))
        points.forward(4)
        screen.update()
        sleep(0.001) #move the turtle that displays the points smoothly across the screen
    screen.tracer(True)

    #animate the fireworks
    for i in range(int(point/10)):
        x=(randint((-200/advancement),(200/advancement)))*advancement
        y=(randint((-120/advancement),(130/advancement)))*advancement
        firework(x,y)
    
    screen.tracer(False)
    points.color('dark green')
    points.goto(-75,-40)
    points.write("HIGH SCORE: "+highscore, font=('Impact',18,'bold'))
    screen.tracer(True)
#Function to animate a firework
def firework(x,y):
    screen=Screen()
    screen.tracer(False)
    screen.colormode(255)
    fire=Turtle()
    fire.ht()

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

    while colour!=(255,255,255): 
        for i in range(n):
            corners[i].clear()
            corners[i].forward(5)
            corners[i].dot(5,colour)
        colour=colorupdate(colour)
        sleep(0.01)
        screen.update() #move forward down the trail, while fading towards white
    for i in corners:
        i.clear()
    screen.tracer(True)
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
#Function to create special pill!
def special_pill():
    screen=Screen()
    screen.tracer(False)

    special.penup()
    x=(randint((-200/advancement),(200/advancement)))*advancement
    y=(randint((-120/advancement),(130/advancement)))*advancement
    while getcolor(x,y)=='orange' or getcolor(x,y)=='green':
        x=(randint((-200/advancement),(200/advancement)))*advancement
        y=(randint((-120/advancement),(130/advancement)))*advancement

    special.setpos(x,y)
    special.dot(10,"red")

    screen.tracer(True)
#Function to setup timer for special pill
def timer_setup():
    screen=Screen()
    screen.tracer(False)
    timer.color("red")
    timer.goto(150,140)
    timer.setheading(0)
    for i in range(10):
        timer.forward(5)
        timer.stamp()
    screen.tracer(True)
#Function to draw a square with a letter inside
def square(side,letter):
    screen=Screen()
    screen.tracer(False)
    x=draw.xcor()
    y=draw.ycor()
    draw.pendown()
    draw.setheading(90)
    draw.forward(side)
    draw.setheading(0)
    draw.forward(side)
    draw.setheading(270)
    draw.forward(side)
    draw.setheading(180)
    draw.forward(side)
    draw.penup()
    draw.goto(x+9*side/32,y+side/8)
    draw.write(letter)
    screen.tracer(True)
#Function to calculate the highest score
def high_score():
    with open('scores.txt') as data:
        data2=data.read() #opening the file in readlines mode
        data.closed #closing the file
    data2=data2.split()
    data3=[]
    for i in data2:
        data3.append(i+"\n")
    data3.append(str(total)+"\n")
    with open('scores.txt','w') as file:
        file.writelines(data3)
        file.closed
    with open('scores.txt') as scores2:
        scores=scores2.read()
        scores2.closed
    scores=scores.split()
    int_scores=[]
    for i in scores:
        int_scores.append(int(i))
    return(str(max(int_scores)))

##NECESSARY VARIABLES
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
num_special=0 #number of special pills on screen
start_pill_time=0 #value to store pill time
screen=Screen()
prev_time=0
move_delay=20

setup(450,340) #initial setup
head=Turtle()
food=Turtle()
draw=Turtle()
points=Turtle() 
special=Turtle()
timer=Turtle()

initialization()
food_coor=food_gen() #generating food

while game!="start" and game!='end':
    start=input("Should the game start (Y/N)?").lower() #ask for input start, so that the user is in the terminal
    if start=='y':
        game='start'
    elif start=='n':
        game='end' 

start_time=int(time()) #time at beginning of game
screen.tracer(False)
for i in range(52):
    draw.undo()
screen.tracer(True)

while game!="end":
    if head.xcor()>=204 or head.xcor()<-204 or head.ycor()>=134 or head.ycor()<=-124:
        game='end' #lose game if you leave board

    if kbhit():
        ui=getch() #recieve input
        if ui in [b'w',b'a',b's',b'd'] and ui!=user_direction and user_direction!=invalid[ui]: #check if the iser direction is valid
            user_direction=ui
            defined_direction=list(str(user_direction))[2] #assign the direction
            direction_change(defined_direction)  #change direction

    advance(length,move_delay) #move snake
    move_delay+=0.3
    color_under=getcolor(head.xcor(),head.ycor()) #check what color is underneath

    if (head.position()==food_coor or color_under=='orange'): #check for food, and increase length if food is consumed
        food.clear()
        length+=2
        food_coor=food_gen()
        total+=4
        point_update(total)
    
    current_time=int(time()-start_time) #timer at this turn 
    if current_time % 30 == 15 and num_special==0: #create a special pill and its timer every 30 seconds
        start_pill_time=int(time()-start_time)
        screen.tracer(False)
        special_pill()
        num_special+=1
        timer_setup()
        screen.tracer(True)
    if start_pill_time!=0:
        timer.color('white')
        if prev_time!=current_time-start_pill_time: #to assure it only updates once per second for 10 seconds
            screen.tracer(False)
            timer.setheading(180)
            timer.stamp()
            timer.forward(5)
            screen.tracer(True) #erase a tenth of the timer
            prev_time=current_time-start_pill_time #update previous time for comparison
        if current_time-start_pill_time>=10: #after 10 seconds, clear the pill
            screen.tracer(False)
            start_pill_time=0
            special.clear()
            num_special=0
            timer.clear()
            screen.tracer(True)

    if color_under=='red': #points added for reaching pill, and clearing it out
        screen.tracer(False)
        special.clear()
        timer.clear()
        total+=10*(10-(current_time-start_pill_time))
        length+=(10-(current_time-start_pill_time))
        start_pill_time=0
        num_special=0
        point_update(total)
        screen.update()
        screen.tracer(True)

    if color_under=='green' or color_under=='black': #end game
        game='end'


highest_score=high_score()
clearscreen()
endgame(total,highest_score) #end of game animations
screen.exitonclick()