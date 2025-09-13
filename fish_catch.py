#fish_cathch.py: calculate fish catch for test.zervant.com user dasko_se@zervant.com.

import random

x = 0
y = 0
z = 0

#Average weight of fish: notice that this gives you a random decimal!
x = random.uniform(3.2,10.5)

#Number of fish.
y = random.randint(3,10)

z = x * y

print "\nAverage fish weight(kg): ",round(x, 2)
print "Number of fish: ",y
print "\nTotal fish weight today(kg): ",round(z, 2)
