#Craps_Dev_Stats.py: Let's you play again without restarting the program.

import random

#Initialize variables.
roll = 0
c = 0
play = 0

#Start game: push "0" to roll, to play.
while play < 1:

    play = int(raw_input("\nEnter 0 to roll (1 to quit):"))
    print ""

    if play >= 1:
        break

    #Generate the dice roll numbers and add. 
    x = random.randint(1,6)
    y = random.randint(1,6)
    z = x + y

    print "\nYou rolled: ",x,"+",y,"is:",z

    #The following are the results of win/lose on the first roll.  The app
    #breaks after rolling 2,3,7,11 or 12.  The flow continues for other numbers.
    while roll <= 1:
      
        if z == 7:
            print "\n7 on the first roll! YOU WIN!\n"
            break
        elif z == 11:
            print "\n11 on the first roll! YOU WIN!\n"
            break
        elif z == 2:
            print "\n2 on the first roll! YOU LOSE.\n"
            break
        elif z == 3:
            print "\n3 on the first roll! YOU LOSE.\n"
            break
        elif z == 12:
            print "\n12 on the first roll! YOU LOSE.\n"
            break 
        else:  
            roll = roll + 1
            print "\nROLL AGAIN!"


    #This handles second or more rolls.
    while c != 7 or c != z:

        if roll <= 1:
            break

        a = random.randint(1,6)
        b = random.randint(1,6)

        c = a + b

        print "\nThe reroll is: ",a,"+",b,"=",c
        
        if c == 7:
            print "\n7 on the second or more roll! YOU LOSE!\n"
            break
            roll = roll + 1
        elif c == z:
            print "\nThe rolls match: YOU WIN!!"
            break
            roll = roll + 1
        else:
            print "\nROLL AGAIN!"
            #break

    #Ask if the User wants to play again.  
    roll = int(raw_input("\nPress 1 to continue or 0 to quit: "))    


    

    

    

    
