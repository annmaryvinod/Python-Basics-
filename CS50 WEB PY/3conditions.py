n = (input("Number: "))

if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")        





    # Why does this code not work ?


    # 1. n = input("Number : ")  takes all values of n as string
    # if you look at the error msg in terminal, you will see it is a TypeError
    # 2. i.e, the comparison with <,> do not work between a str and an integer.
    # more specific : n is a str while 0 is an int


    # 4conditions.py has the solution to this!



