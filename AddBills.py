#AddBills.py: this keeps a running amount.
#Idea: Have the script give you a running amount every 5 entries.

x = 1
sum = 0
runsum = 0

while x != 0:
    x = float(raw_input("Enter an amount:"))
    sum = sum + x

print "\nThe total is: ",sum
