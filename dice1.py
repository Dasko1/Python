#dice2.py:roll a dice 6,000 times; each side should be around 1,000.

import random

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
#The number of times the dice is rolled.
count = 0
print ""

while count < 6000:

  #roll dice here
  x = random.randint(1,6)

  if x == 1:
    one = one + 1
  if x == 2:
    two = two + 1
  if x == 3:
    three = three + 1
  if x == 4:
    four = four + 1
  if x == 5:
    five = five + 1
  if x == 6:
    six = six + 1
  count = count + 1


print "1:",one
print "2:",two
print "3:",three
print "4:",four
print "5:",five
print "6:",six