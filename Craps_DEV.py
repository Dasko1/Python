#Craps_DEV: plays a simple game of craps pretty well.

import random

roll = 0
c = 0

x = random.randint(1,6)
y = random.randint(1,6)

z = x + y

print "\nYou rolled: ",x,"+",y,"is:",z

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
        #break



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

    

    

    
