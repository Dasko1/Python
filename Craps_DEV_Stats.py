#Craps_Dev_Stats.py: Let's you play again without restarting the program.

import random

#Initialize variables.
roll = 0
c = 0
play = 0
win = 0
loss = 0

#Start game.
while play < 1:

    play = int(raw_input("\nEnter 0 to roll (1 to quit): "))

    if play >= 1:
        break

    #Generate the dice roll numbers and add. 
    x = random.randint(1,6)
    y = random.randint(1,6)
    z = x + y

    print "\nYou rolled: ",x,"+",y,"is:",z
    
    while roll <= 1:
      
        if z == 7:
            print "\n7 on the first roll! YOU WIN!\n"
            win = win + 1
            break
        elif z == 11:
            print "\n11 on the first roll! YOU WIN!\n"
            win = win + 1
            break
        elif z == 2:
            print "\n2 on the first roll! YOU LOSE.\n"
            loss = loss + 1
            break
        elif z == 3:
            print "\n3 on the first roll! YOU LOSE.\n"
            loss = loss + 1
            break
        elif z == 12:
            print "\n12 on the first roll! YOU LOSE.\n"
            loss = loss + 1
            break 
        else:  
            roll = roll + 1
            #break


    #This handles second or more roll.
    while c != 7 or c != z:

        if roll <= 1:
            break

        a = random.randint(1,6)
        b = random.randint(1,6)

        c = a + b

        print "\nThe reroll is: ",a,"+",b,"=",c
        
        if c == 7:
            print "\n7 on the second or more roll! YOU LOSE!\n"
            loss = loss + 1
            break
            roll = roll + 1
        elif c == z:
            print "\nThe rolls match: YOU WIN!!"
            win = win + 1
            break
            roll = roll + 1
        else:
            print "\nROLL AGAIN!"
            #break

    #Show won/loss record.
    print "\nGames won:",win
    print "\nGames lost:",loss
    #Ask if the User wants to play again.  
    roll = int(raw_input("\n\nPress 1 to continue or 0 to quit: "))    


    

    

    

    
