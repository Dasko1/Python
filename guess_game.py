import random

try1 = 0

to_guess_num = random.randint(1, 10)

while try1 <= 2:
    my_guess = input("Guess a 1-10 number (3 tries): ")
    
    if int(my_guess) == to_guess_num:
        print("\nCorrect! YOU WIN!! The number really was: " + str(to_guess_num) + "!")
        break
            
    else:
        print("\nNot quite: try again!")
        try1 += 1
        print("Try count: " + str(try1))
        if try1 == 3:
            print("\nYou lost! The number to guess was: " + str(to_guess_num))
