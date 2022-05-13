# Define the variables below. Print the types of each variable. What is the sum of your variables?
# (Hint: use a type conversion function.) What datatype is the sum?
print("===1 TASK===")
a=4
b=99.11

print(type(b))
print(type(a))
print(type(a+b))
print(a+b)

print("===2 TASK===")
# Exercise: Find the last position of a given substring
s="Hello World!"
print(s [len(s)-1 : len(s) ])

print("===3 TASK===")
# Write a program to find the last position of a substring "Emma" in a given string.
m="Emma"
theLatest=len(m)
print(m [theLatest-1 : theLatest])

print("===4 TASK===")
# Exercise: Return the count of a given substring from a string
h="88"
n="6"
l=int("7")+int("7")
print(int(h)+int(n),  l, sep=" and ")

f=3
r=5
print("A","B",f+r, sep=" ")


print("===5 TASK===")
# Exercise: Insert the correct syntax to add a placeholder for the age parameter
age=55
print(f'My age is {age} ')

print("===6 TASK===")
# Exercise: Return the string without any whitespace at the beginning or the end
h="   test for whitespaces   .  "
print(h.rstrip())
print(h.lstrip())
print(h.strip())