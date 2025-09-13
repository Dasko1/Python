#Add7FirstRoll.py:generate 2 random dice rolls and say if they add up to 7.

import random

roll = 0

x = random.randint(1,6)
y = random.randint(1,6)

z = x + y

while roll < 1:

    if z == 7:
        print "\n7 on the first roll! YOU WIN!\n"
        break
    if z == 11:
        print "\n11 on the first roll! YOU WIN!\n"
        break
    if z == 2:
        print "\n2 on the first roll! YOU LOSE.\n"
        break
    if z == 3:
        print "\n3 on the first roll! YOU LOSE.\n"
        break
    if z == 12:
        print "\n12 on the first roll! YOU LOSE.\n"
        break
    else:
        print "\nYou rolled: ",x,"+",y,"is:",z
        roll = roll + 1

