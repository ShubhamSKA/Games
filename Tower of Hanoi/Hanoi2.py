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

tower1=sorted(list(set(input("Enter the numbers in the first tower: ").split())))
tower1.reverse()
for i in range(len(tower1)):
    tower1[i]=int(tower1[i])
tower2=sorted(list(set(input("Enter the numbers in the second tower: ").split())))
tower2.reverse()
for i in range(len(tower2)):
    tower2[i]=int(tower2[i])
tower3=sorted(list(set(input("Enter the numbers in the third tower: ").split())))
tower3.reverse()
for i in range(len(tower3)):
    tower3[i]=int(tower3[i])



n=len(tower1)+len(tower2)+len(tower3)

previous = [tower1,tower2,tower3]
current  = [tower1,tower2,tower3]

steps=0

system('cls')
print_array(current,n)
sleep(0.5)

while current!=[[],[],list(range(n,0,-1))]:
    sleep(0.01)
    system('cls')
    moves=possible_moves(current)
    previous.append(deepcopy(current))
    if move(current,moves,1) not in previous:
        current=deepcopy(move(current, moves,1)) 
    else:
        current=deepcopy(move(current , moves, 0))
    print_array(current,n)
    steps+=1
    if len(previous)>0:
        del previous[0]
    print("\nNumber of steps taken:", steps)  
