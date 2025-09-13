#Fibonacci.py: enter a number and get that range in the Fibonacci series.

numbers = raw_input("How many numbers would you like to display: ")

a = 1
b = 1

print ""
print a
print b

for d in range(int(numbers)):
    c = a + b 
    print c
    a = b
    b = c

print ""
