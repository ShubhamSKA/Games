from time import *
from os import *

def printBoard(loc,length):
    x=loc[0]
    y=loc[1]

    middle=("║"+' '*72+"║")
    print("╔════════════════════════════════════════════════════════════════════════╗")
    for i in range(9):
        print(middle)
    print("║"+' '*(x-length)+westsnake(length)+' '*(72-x)+"║")
    for i in range(9):
        print(middle)
    print("╚════════════════════════════════════════════════════════════════════════╝")
def pause(secs):
    init_time = time()
    while time() < init_time+secs: 
        pass
def westsnake(length):
    body =("○"*(length-1)+"◑")
    return body
def westmove(loc,length):
    x=loc[0]
    y=loc[1]
    while(x<72):
        x+=1
        system('cls')
        printBoard((x,y),length)
        pause(0.1)
def location(num):
    y=int((num-1)/72)
    x=num%72
    return(x,y)
    

westmove((10,8),5)