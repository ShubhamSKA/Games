from os import system
from time import sleep
from copy import deepcopy

def print_array(array,tallest_len):
    first=array[0]
    second=array[1]
    third=array[2]
    while tallest_len>=1:
        if len(first)>=tallest_len:
            print("{0:<3}".format(first[tallest_len-1]), end='')
        else:
            print("   ", end='')
        if len(second)>=tallest_len:
            print("{0:<3}".format(second[tallest_len-1]), end='')
        else:
            print("   ", end='')
        if len(third)>=tallest_len:
            print("{0:<3}".format(third[tallest_len-1]), end='')
        else:
            print("   ", end='')
        print('')
        tallest_len-=1
    print('__ __ __')
def possible_moves(array):
    def check_which(tow1,tow2):
        try:
            a=tow1[-1]
        except:
            a=100
        try:
            b=tow2[-1]
        except:
            b=100
        if a==b:
            return(0)
        elif a>b:
            return(1)
        else:
            return(2)
    first=array[0]
    second=array[1]
    third=array[2]
    possibilities=[]
    possibilities.append(check_which(first,second))
    possibilities.append(check_which(second,third))
    return(possibilities)
def move(array, possibilities, moveselect):
    first=deepcopy(array[0])
    second=deepcopy(array[1])
    third=deepcopy(array[2])
    a=possibilities[moveselect]
    if moveselect==0:
        if a==0:
            post_move=[first,second,third]
        if a==1:
            first.append(second[-1])
            del second[-1]
        if a==2:
            second.append(first[-1])
            del first[-1]
    elif moveselect==1:
        if a==0:
            post_move=[first,second,third]
        if a==1:
            second.append(third[-1])
            del third[-1]
        if a==2:
            third.append(second[-1])
            del second[-1]
    post_move=[first,second,third]
    return post_move
    
n=6 #number of disks on the tower - be careful when making the number too large, as it can cause the list to have an absurd amount of elements, slowing down python
previous=[[list(range(n,0,-1)),[],[]]] #list of all previous moves -> need to optimize, as it can quickly get absurdly large
current=[list(range(n,0,-1)),[],[]] #current state of tower of hanoi
steps=0

system('cls')
print_array(current,n)
sleep(0.5)

while current!=[[],[],list(range(n,0,-1))]:
    sleep(10/(3**n-1)) #so that it is solved in 10 seconds
    system('cls')
    moves=possible_moves(current)
    previous.append(deepcopy(current))
    if move(current,moves,1) not in previous:
        current=deepcopy(move(current, moves,1)) 
    else:
        current=deepcopy(move(current , moves, 0))
    print_array(current,n)
    steps+=1
    print("\nNumber of steps taken:", steps)   #will eventually take 3^n-1 steps
