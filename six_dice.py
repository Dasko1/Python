#six_dice.py: according to the numbers, if you want to make certain that any
#one number is rolled, you need to roll six dice.  If you want to verify that
#the number one, for example, comes up in a roll, you will be assured of it if
#you roll six dice at once.

import random

print "Here 6 dice rolled at once: is there a 1?"

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
dice3 = random.randint(1,6)
dice4 = random.randint(1,6)
dice5 = random.randint(1,6)
dice6 = random.randint(1,6)

print dice1
print dice2
print dice3
print dice4
print dice5
print dice6

