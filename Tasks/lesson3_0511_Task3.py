# Task 3
# The name check.
# Write a program that has a variable with your name stored (in lowercase)
# and then asks for your name as input. The program should check
# if your input is equal to the stored name even if the given name has another case,
# e.g., if your input is “Anton” and the stored name is “anton”, it should return True.


input=input()

myName="Yuliia"
print("Hello, my name is Yuliia")
newMynameInput=input.lower()
newMynameStored=myName.lower()

print("The first way. Result:")
if newMynameInput==newMynameStored:
    print("The names are the same")
else:
    print("The names are not the same")

print("The second way. Result:")
i=0;
while(i < len(newMynameStored)):
    if newMynameStored[i]==newMynameInput[i]:
        i = i + 1
    else:
        print("The names are Not the same")
        i = i + 1
