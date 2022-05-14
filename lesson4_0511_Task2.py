# Task 2
# The valid phone number program.
# Make a program that checks if a string is in the right format for a phone number.
# The program should check that the string contains only numerical characters
# and is only 10 characters long. Print a suitable message depending on the outcome of the string evaluation.


input=input("Type a number")

if len(input)==10:
    print(input)
    for i in input:
        if i.isnumeric()==True:
            continue
        else:
            print("Number contain not only numeric")
            break
else:
    print("Number contain more or less then 10 numeric")


