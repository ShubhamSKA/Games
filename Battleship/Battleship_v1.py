from random import randint
from copy import deepcopy

def start():
    print("               ~ Welcome to Battleship! ~\n")
    print("ChatGPT has gone rogue and commandeered a carrier strike group. It's on a mission to take over the world. We've located the stolen ships, but we need your superior intelligence to help us sink them before it's too late.\n")
def main_menu():
    print("Menu:\n  1 : Instructions\n  2 : New game\n  3 : Hall of Fame\n  4 : Quit")
    inp=input("What would you like to do? ")
    while inp not in ['1','2','3','4']:
        print("\nInvalid selection. Please choose a number from the menu.\n")
        print("Menu:\n  1 : Instructions\n  2 : New game\n  3 : Hall of Fame\n  4 : Quit")
        inp=input("What would you like to do? ")
    return(int(inp))
def hall_of_fame():
    with open('battleship_hof_full.txt') as data:
        data2=data.readlines()
        data.closed
    print("\n--- Hall of Fame ---")
    print(" ## : Accuracy : Played")
    for i in range(len(data2)):
        print('{:>3} '.format(i+1), end='')
        data2[i]=data2[i].split(',')
        data2[i][0]=100*float(data2[i][0])
        print(':   {:.2f}%'.format((data2[i][0])), end = ' :')    
        print(' '+str(data2[i][1]), end='')
    print('')
def generate_ship(length):
    coord=[]
    dir=randint(1,2)
    if dir==1:
        column=randint(0,9-length)
        row=randint(0,9)
        position=10*row+column
        for i in range(length):
            coord.append(position)
            position+=1
    if dir==2:
        row= randint(0,9-length)
        column=randint(0,9)
        position=10*row+column
        for i in range(length):
            coord.append(position)
            position+=10
    return(coord)
def generate_board_locations():
    global all_used
    global locations
    locations['C']=generate_ship(5)
    for i in locations['C']:
        all_used.append(i)

    temp=generate_ship(4)
    while check_if_in(all_used,temp)==True:
        temp=generate_ship(4)
    locations['B']=temp
    for i in temp:
        all_used.append(i)

    temp=generate_ship(3)
    while check_if_in(all_used,temp)==True:
        temp=generate_ship(3)
    locations['D']=temp
    for i in temp:
        all_used.append(i)

    temp=generate_ship(3)
    while check_if_in(all_used,temp)==True:
        temp=generate_ship(3)
    locations['S']=temp
    for i in temp:
        all_used.append(i)
    
    temp=generate_ship(2)
    while check_if_in(all_used,temp)==True:
        temp=generate_ship(2)
    locations['P']=temp
    for i in temp:
        all_used.append(i)
    return locations
def generate_board(locations):
    board=[]
    for i in range(100):
        board.append('~')
    for i in list(locations.keys()):
        for coor in locations[i]:
            board[coor]=i
    return(board)
def check_if_in(principal, subsidiary):
    var=0
    for i in subsidiary:
        if i in principal:
            var+=1
    if var>0:
        return True
    else:
        return False
def print_board(board):
    print('')
    print("   0  1  2  3  4  5  6  7  8  9")
    letters=['A','B','C','D','E','F','G','H','I','J']
    for i in range(len(board)):
        if i%10==0:
            print(letters[int(i/10)], end='  ')
        if i%10==9:
            print(board[i])
        else:
            print(board[i], end='  ')   
def outer_board(board, pos, innerboard):
    global attacks
    if pos in attacks:
        print("\nYou already attacked this spot, try again!\n")
    elif innerboard[pos]=='~':
        print("\nmiss\n")
        board[pos]='o'
        attacks.append(pos)
    else:
        print("\nIT'S A HIT!")
        board[pos]='x'
        attacks.append(pos)
    return board
def getpos():
    acceptable=False
    val={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9}
    print('')
    while acceptable==False:
        position=input("Where should we target next (q to quit)? ")
        if position =='q':
            print("\ngoodbye\n")
            quit()
        elif len(position)!=2:
            print("Please enter exactly two characters.")
        else:
            position=[*position]
            if (position[0].lower()) not in val.keys():
                print('Please enter a location in the form "G6".')
            else:
                acceptable=True
    actual_position=int(position[1])+10*val[position[0].lower()]
    return actual_position
def check_ship(pos):
    global locations
    for i in locations.keys():
        if pos in locations[i]:
            return i
def check_hall(percentage):
    subdata=[]
    with open('battleship_hof_full.txt') as data:
        data2=data.readlines()
        data.closed
    for i in range(len(data2)):
        data2[i]=data2[i].split(',')
        data2[i][0]=(int(float(data2[i][0])*100000)/1000)
    for i in data2:
        subdata.append(i[0])
    if percentage<data2[-1][0]:
        print("Your targeting accuracy was {:.2f}%.".format(percentage))
    else:
        print("Congratulations, you have achieved a targeting accuracy of {:.2f}% and earned a spot in the Hall of Fame.".format(percentage))
        user=input("Enter your name: ")
        count=0
        while percentage<=data2[count][0]:
            count+=1
        data2.insert(count,[percentage,user+'\n'])
        if len(data2)>10:
            del data2[-1]
        with open("battleship_hof_full.txt",'w') as data:
            for i in range(len(data2)):
                data.write('{:.4f},'.format(data2[i][0]/100)+data2[i][1])
            data.closed
        hall_of_fame()


game=1
ui=main_menu()
attacks=[]
all_used=[]
succesful=0
outerboard=['~']*100
locations={}
prev_succesful=0
attacked_amount={'C':[0,5], 'B':[0,4],'D':[0,3],'S':[0,3],'P':[0,2]}
ship_conv={'C':'Carrier','B':'Battleship','D':'Destroyer','S':'Submarine','P':'Patrol Boat'}
turns=0

start()
while ui!=4:
    while ui not in [4,2]:
        if ui==1:
            start()
            ui=main_menu()
        elif ui==3:
            hall_of_fame()
            ui=main_menu()
    if ui==2:
        locs=generate_board_locations()
        innerboard=generate_board(locs)
        while game==1:
            turns+=1
            prev_succesful=succesful
            succesful=0
            print_board(outerboard)
            pos=getpos()
            outerboard=outer_board(outerboard,pos,innerboard)
            for position in attacks:
                if position in all_used:
                    succesful+=1
            if prev_succesful != succesful:
                attacked_ship=check_ship(pos)
                attacked_amount[attacked_ship][0]+=1
                if attacked_amount[attacked_ship][0]==attacked_amount[attacked_ship][1]:
                    print("The enemy's {} has sunk.".format(ship_conv[attacked_ship]))
            if succesful>=17:
                print("You've sunk the enemy fleet!\nHumanity has been saved from the threat of AI.\n\nFor now ...\n")
                percentage=(int(turns/17*10000)/1000)
                check_hall(percentage)
                game=0
if ui==4:
        print("\nGoodbye")