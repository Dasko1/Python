# Writes "Finland" backwards like that code challenge in interview.

reverse_this = "Finland"

print("Reverse this word: ",reverse_this)

x = [reverse_this]

y = list(''.join(x))

y.reverse()

z = (''.join(y))
print("\nThe reverse is: ",z)


