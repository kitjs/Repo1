# Task 1
# The Guessing Game.
# Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.


import random

computer=random.randint(0,10)
print("Computer: ", computer)

inp=input("Type a number between 1 and 10")

inpItr = int(inp)

if inpItr == computer:
    print("You are true!")
elif inpItr != computer:
    print("You are NOT true!")
print("Computer: ", computer)




# Task 2
# The birthday greeting program.
# Write a program that takes your name as input, and then your age as input and greets you with the following:
# “Hello <name>, on your next birthday you’ll be <age+1> years”

age= input("type your current age\n")
name = input("type your name\n")
print(f"Hello {name}, on your next birthday you’ll be {int(age)+1} years")

# Task 3
# Words combination
# Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
# For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters 
# 'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
# Tips: Use random module to get random char from string)
import random

import random
inp=input("typ a string:\n")

print(''.join(random.sample(inp,len(inp))))
print(''.join(random.sample(inp,len(inp))))
print(''.join(random.sample(inp,len(inp))))
print(''.join(random.sample(inp,len(inp))))
print(''.join(random.sample(inp,len(inp))))
x=range(1,10)
print(x)

# Task 4
# The math quiz program
# Write a program that asks the answer for a mathematical expression,
# checks whether the user is right or wrong, and then responds with a message accordingly.


computer_result = 6*8-7+6/2
user_result = input('Type a result of  "6*8-7+6/2" \nInput an answer\n ')
if user_result.isalpha():
    print("The answer must be a number")

else:
    if float(user_result) == computer_result:
        print("You is correct")
    else:
        print(f"You are wrong. Result is {computer_result}")
