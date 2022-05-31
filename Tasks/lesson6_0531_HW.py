# Task 1
# The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers

# import  random
# t=0
# list=[]
# while t<10:
# #    list.insert(t,random.randint(1,55))
#     list.append(random.randint(1,55))
#     t=t+1
#
# print(list)


# Task 2
# Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10,
# and make a third list containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

# import  random
# t=0
# m=0
# list_1=[]
# list_2=[]
#
# while t<10:
#     list_1.append(random.randint(1,11))
#     t=t+1
# print(list_1)
#
# while m<10:
#     list_2.append(random.randint(1,11))
#     m=m+1
# print(list_2)
#
#
# set_1= set(list_1)
# set_2=set(list_2)
#
# setAll=set_1|set_2
# print(setAll)


# Task 3
# Extracting numbers.
# Make a list that contains all integers from 1 to 100,
# then find all integers from the list that are divisible
# by 7 but not a multiple of 5, and store them in a separate list.
# Finally, print the list.
# Constraint: use only while loop for iteration

# import  random
# t=0
# list=[]
# while t<100:
# #    list.insert(t,random.randint(1,55))
#     list.append(t+1)
#     t=t+1
#
# print(list)
#
# m=0
# list_div5 =[]
# while m<100:
#     if int(list[m]) % 7 == 0 and  int(list[m]) % 5 != 0:
#         print(list[m])
#         list_div5.append(m+1)
#     else:
#         #что можно здесь написать вместо принта??
#         print("")
#     m=m+1
# print(list_div5)