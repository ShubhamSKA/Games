##IMPORTS
#region
from turtle import *
from msvcrt import kbhit,getch
from random import randint
from math import ceil
from time import sleep, time
from os import system
#endregion

###ALL FUNCTION DEFINITIONS
#region
#Function that defines where the food will appear, and draws it
def food_gen():
    screen=Screen()
    screen.tracer(False)

    food.penup()

    x=(randint((-200/advancement),(200/advancement)))*advancement
    y=(randint((-120/advancement),(130/advancement)))*advancement
    canvas=getcanvas()
    ids=canvas.find_overlapping(x-2.5,-(y+2.5),x+2.5,-(y-2.5))
    while (len(ids))!=0: #making sure the food does not appear on the snake or on pill
        x=(randint((-200/advancement),(200/advancement)))*advancement
        y=(randint((-120/advancement),(130/advancement)))*advancement
        ids=canvas.find_overlapping(x-2.5,-(y+2.5),x+2.5,-(y-2.5))
    
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
    wall.width(3)

    food.ht()
    head.ht()
    ht()
    draw.ht()
    points.ht()
    special.ht()
    timer.ht()
    mine.ht()
    wall.ht()

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
    draw.goto(-32-40,10)
    square(20,'A')
    draw.goto(-10-40,10)
    square(20, 'S')
    draw.goto(12-40,10)
    square(20,'D')
    draw.goto(-10-40,32)
    square(20,'W')
    draw.goto(-90,55)
    draw.write("Go to terminal and type in the mode to start")
    draw.goto(10,10)
    square(20,2)
    draw.goto(32,10)
    square(20,3)
    draw.goto(54,10)
    square(20,0)
    draw.goto(32,32)
    square(20,1)
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
    points.goto(-85,-40)
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
    canvas=getcanvas()
    ids=canvas.find_overlapping(x-5,-(y+5),x+5,-(y-5))
    while (len(ids))!=0: #making sure the food does not appear on the snake or on pill
        x=(randint((-200/advancement),(200/advancement)))*advancement
        y=(randint((-120/advancement),(130/advancement)))*advancement
        ids=canvas.find_overlapping(x-5,-(y+5),x+5,-(y-5))
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
#Function to draw a square with a symbol inside
def square(side,object):
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
    if type(object)==str:
        draw.goto(x+9*side/32,y+side/8)
        draw.write(object)
    elif type(object)==int:
        draw.goto(x+side/2,y+side/2)
        draw_arrow(object)
    screen.tracer(True)
#Function to calculate the highest score ever on the computer
def high_score(filename):
    try:
        with open(filename) as data:
            data2=data.read() #opening the file in read mode
            data.closed #closing the file
        data2=data2.split()
    except:
        with open(filename,'w') as file:
            file.writelines("0\n")
            file.closed
        with open(filename) as data:
            data2=data.read() #opening the file in read mode
            data.closed #closing the file
        data2=data2.split()
    data3=[]
    for i in data2:
        data3.append(i+"\n")
    data3.append(str(total)+"\n")
    with open(filename,'w') as file:
        file.writelines(data3)
        file.closed
    with open(filename) as scores2:
        scores=scores2.read()
        scores2.closed
    scores=scores.split()
    int_scores=[]
    for i in scores:
        int_scores.append(int(i))
    return(str(max(int_scores)))
#Function to get gameplay mode and start the game
def modeandstart():
    system('cls')
    screen=Screen()
    modeofgame=0
    while modeofgame not in [1,2,3]:
        try:
            modeofgame=int(input("Select the game mode:\n1-Normal\n2-Mine\n3-Walls\n"))
            if modeofgame not in [1,2,3]:
                print("That is not a valid game mode.")
        except:
            modeofgame=0
            print("That is not a valid game mode!")
    system('cls')
    screen.tracer(0)
    timer.penup()
    color_list=['red','gold','chartreuse']
    i=3
    while i>0:
        timer.goto(head.xcor(), head.ycor()+10)
        timer.color(color_list[3-i])
        t=0
        while t<10:
            timer.write(str(i)+"...",font=('Arial',int((t+4)/2),'normal'))
            t+=1
            update()
            sleep(0.1)
            timer.clear()
        i-=1
    screen.tracer(1)
    return (modeofgame)
#Function to generate mines
def mine_gen():
    screen=Screen()
    screen.tracer(False)

    mine.penup()

    x=(randint((-200/advancement),(200/advancement)))*advancement
    y=(randint((-120/advancement),(130/advancement)))*advancement
    canvas=getcanvas()
    ids=canvas.find_overlapping(x-4,-(y+4),x+4,-(y-4))
    while (len(ids))!=0: #making sure the food does not appear on the snake or on pill
        x=(randint((-200/advancement),(200/advancement)))*advancement
        y=(randint((-120/advancement),(130/advancement)))*advancement
        ids=canvas.find_overlapping(x-4,-(y+4),x+4,-(y-4))
    mine.setpos(x,y)
    mine.dot(8,"black")
    for i in range(8):
        mine.pendown()
        mine.setheading(i*360/8)
        mine.forward(6)
        mine.setpos(x,y)
    update()
    screen.tracer(True)
#Function to generate walls
def wall_gen():
    overlap=1
    screen=Screen()
    canvas=getcanvas()
    screen.tracer(0)
    wall.penup()
    set_direction=90*(randint(0,3))
    wall.setheading(set_direction)
    set_length=advancement*(randint(4,15))
    while overlap!=0:
        overlap=0
        x=(randint((-200/advancement),(200/advancement)))*advancement
        y=(randint((-120/advancement),(130/advancement)))*advancement
        wall.goto(x,y)
        for i in range(set_length):
            wall.forward(1)
            xcheck=wall.xcor()
            ycheck=wall.ycor()
            ids=canvas.find_overlapping(xcheck-1,-(ycheck+1),xcheck+1,-(ycheck-1))
            overlap+=len(ids)
    wall.goto(x,y)
    wall.pendown()
    wall.forward(set_length)
    wall.penup()
    screen.tracer(1)
#Function to draw arrows
def draw_arrow(direct):
    screen=Screen()
    screen.tracer(0)
    draw.setheading(90*direct)
    draw.pendown()
    draw.forward(8)
    posit=draw.position()
    draw.right(150)
    draw.forward(4)
    draw.goto(posit)
    draw.setheading(90*direct)
    draw.left(150)
    draw.forward(4)
    draw.goto(posit)
    draw.penup()
    screen.tracer(1)
#Function to replace the stamp made by timer
def timer_stamp():
    screen=Screen()
    screen.tracer(0)
    timer.fillcolor('white')
    timer.pencolor('white')
    timer.pendown()
    timer.begin_fill()
    for i in range(4):
        timer.forward(5)
        timer.right(90)
    timer.end_fill()
    timer.penup()
#endregion

##NECESSARY VARIABLES
#region
tails=[] #list storing all the parts of the tail
game=0 #intitial value of game
direction='d' #initial value for direction
user_direction=0 #initial value for valid input direction
invalid={'w':'s','a':'d','s':'w','d':'a'} #dictionary of invalid turns
arrow_equivalencies={b'H':b'w',b'K':b'a',b'P':b's',b'M':b'd'}
total=0 #number of points
length=10 #length of the snake
velocity=11 #velocity of head
advancement=5 #each advancement of the snake
num_special=0 #number of special pills on screen
start_pill_time=0 #value to store pill time
screen=Screen() #screen
prev_time=0 #time at which the special pill will be produced
move_delay=20 #variable to allow for an increase in speed
mine_time=0 #time at which mine will be produced
uis=[b'd'] #initial value of user inputs
walls_time=0 #time at which wall will be produced
food_eaten=0 #amount of normal food eaten at the given moment
food_till=0 #amount of food eaten by the time the special pill appears
#endregion

##TURTLE SETUP
#region
screen.setup(450,340,900,200) #initial setup
head=Turtle()
food=Turtle()
draw=Turtle()
points=Turtle() 
special=Turtle()
timer=Turtle()
mine=Turtle()
wall=Turtle()
#endregion

##INITIALIZING
#region
initialization()
food_coor=food_gen() #generating food
gamemode=modeandstart()
game='start'

start_time=int(time()) #time at beginning of game
screen.tracer(False)
for i in range(143):
    draw.undo()
screen.tracer(True)
#endregion

###############
###GAME PLAY###
###############
#region
while game!="end":
    if head.xcor()>=204 or head.xcor()<-204 or head.ycor()>=134 or head.ycor()<=-124:
        game='end' #lose game if you leave board
    
    #USER INPUT
    #region
    input_check=0
    uis=([uis[-1]])
    modded_uis=[]
    while input_check==0:
        if kbhit():
                a=getch()
                uis.append(a)
        else:
            input_check=1
    for userinput in uis:
        if userinput==b'\xe0':
            continue
        #print(userinput)
        if userinput in arrow_equivalencies.keys():
            userinput=arrow_equivalencies[userinput]
        userinput=userinput.lower() #recieve input
        userinput=list(str(userinput))[2]
        modded_uis.append(userinput)
    uinput=modded_uis[-1]
    if uinput in ['w','a','s','d'] and uinput!=user_direction and user_direction!=invalid[uinput]: #check if the iser direction is valid
        user_direction=uinput
        #defined_direction=list(str(user_direction))[2] #assign the direction
        direction_change(user_direction)  #change direction
    #endregion
    
    advance(length,move_delay) #move snake
    move_delay+=0.3
    color_under=getcolor(head.xcor(),head.ycor()) #check what color is underneath the snake

    if (head.position()==food_coor or color_under=='orange'): #check for food, and increase length if food is consumed
        food.clear()
        length+=2
        food_coor=food_gen()
        total+=4
        point_update(total)
        food_eaten+=1

    
    current_time=int(time()-start_time) #timer at this turn 
    
    #SPECIAL PILL
    #region
    if current_time % 30 == 15 and num_special==0 and food_eaten>food_till+3: #create a special pill and its timer every 30 seconds
        start_pill_time=int(time()-start_time)
        food_till=food_eaten
        screen.tracer(False)
        special_pill()
        num_special+=1
        timer_setup()
        timer.goto(timer.xcor()+2,timer.ycor()-2)
        timer.isvisible()
        screen.tracer(True)
    if start_pill_time!=0:
        screen.tracer(0)
        timer.color('white')
        screen.tracer(1)
        if prev_time!=current_time-start_pill_time: #to assure it only updates once per second for 10 seconds
            screen.tracer(False)
            timer.setheading(180)
            timer_stamp()
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
        #endregion
    if gamemode==2 and current_time>mine_time:
        mine_time+=22-int(food_eaten/4)
        mine_gen()
    if gamemode==3 and current_time>walls_time:
        walls_time+=45-int(food_eaten/3)
        wall_gen()

    if color_under=='green' or color_under=='black': #end game
        game='end'
#endregion

##END OF GAME
#region
filename='scores.txt'
if gamemode==2:
    filename='mine_scores.txt'
elif gamemode==3:
    filename='wall_scores.txt'
highest_score=high_score(filename)
clearscreen()
endgame(total,highest_score) #end of game animations
screen.exitonclick()
system('cls')
#endregion