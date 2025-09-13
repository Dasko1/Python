#def_Add.py: write add as a function you can call.  If you just enter "add()" in
#the Python Shell, you will get the same result as if you ran this program!

##def add():
##
##    #Ask for 2 numbers and add them!
##    x = 0
##    y = 0
##
##    x = int(raw_input("\nEnter the first number: "))
##    y = int(raw_input("\nEnter the second number: "))
##
##    z = x + y
##
##    print "\nThe sum is:",z
##
###This executes the code in def add():
##def main():
##    add()
##
###This executes the code in def main():
##main()


#You can also write the definition like this: 
def add():
    
    #Ask for 2 numbers and add them!
    x = 0
    y = 0

    x = int(raw_input("\nEnter the first number: "))
    y = int(raw_input("\nEnter the second number: "))

    z = x + y

    print "\nThe sum is:",z

add()
