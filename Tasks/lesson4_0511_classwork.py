# Write a Python program to check whether a letter is a vowel or consonant.

# input=input("Type string")
# for i in input:
#     if i.islower()==True:
#         print(i," is lower")
#     elif i.isupper()==True:
#         print(i, " is uppercase")
#     else:
#         print("not only letters are in string")
#         break

# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. Note : Use 'continue' statement.

# k=1
# while k < 7:
#     if k==3 or k==6:
#         k += 1
#         continue
#     else:
#         print(k)
#         k += 1


# Write a python program to find the sum of all even numbers from 0 to 10

# sum= 0
# b=1
# while b < 11:
#     sum=sum+b
#     print(b)
#     b += 1
# print(sum)

# Finding the average of 5 numbers using while loop

# sum1= 0
# b=0
# while b < 6:
#     sum1=sum1+b
#     print(b)
#     b += 1
# print("average of 5 numbers is "+ sum1/6)

# Finding the factorial of number (with while loop)

factorial= 1
g=1
while g < 6:
    factorial=factorial*g
    print(g)
    g += 1
print("Factorial of",g-1 ," is ",factorial, sep=" ")

# Write a python program to print the square of all numbers from 10 to 20
# (edited)

i=10
while i <=20:
    print('Square is ',i**2)
    i+=1
