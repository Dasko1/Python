# AddBills.py: this keeps a running amount.
# Idea: Have the script give you a running amount every 5 entries.

x = 1
sum1 = 0

while x != 0:
    x = float(input("Enter an amount:"))
    sum1 = sum1 + x

print("\nThe total is: " + str(sum1))
