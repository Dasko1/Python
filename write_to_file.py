#write_to_file.py: write a random number to a file.  This script replaces the
#number; to append a new number at the bottom, see the append_to_file.py script.

#Generate a random number
import random

x = random.randint(1,100)

#Print it to screen or to the Test.txt file, or both if you want.
print x

f = open('Test.txt', 'w')
#Convert the integer to a string.
value = (x)
s = str(value)
f.write(s)
f.close()





