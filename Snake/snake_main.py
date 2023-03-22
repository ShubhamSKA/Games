from msvcrt import *
from time import *

game=0
direction='d'
user_direction=0

while game!='end':
    # Check if there is any user input ready to be read
    if kbhit():
        ui=getch()
        if ui in [b'w',b'a',b's',b'd'] and ui!=user_direction:
            user_direction=ui
            defined_direction=list(str(user_direction))[2]
            print(defined_direction)
            print("the direction is", user_direction)

    # Execute other commands here
    print("Executing other commands...")
    sleep(1)