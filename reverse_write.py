# Writes "Finland" backwards like that code challenge in interview.

reverse_this = "Finland"

print("Reverse this word: ", reverse_this)

print("\nPut the target word to reverse into a list!")
x = [reverse_this]
print(x)

print("\nUse join with space to separate each character!")
y = list(''.join(x))
print(y)

y.reverse()

print("\nYou can now reverse and join the letters back!")
z = (''.join(y))
print("The reverse is: ", z)


