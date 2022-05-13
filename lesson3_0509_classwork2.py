#Write a Python program to convert temperatures to and from celsius, Fahrenheit. Formula : c/5 = (f-32)/9 [ where c = temperature in celsius and f = temperature in Fahrenheit. Expected Output (pay attention to output, students have to practice in string formating for constructing result message): 60°C is 140 in Fahrenheit
#        45°F is 7 in Celsius.
#       Use different string formating!

b=input("""Please, type "F" or if you want to convert from Farengeit \nor "C" if you want to convert from Celcius""")
t = input("Please, type temperature:")


if b in ("F","f"):
    f=int(t)
    print(f,"F is",(f-32)/9, "Celsius" ,sep= " " )

elif b in ("C","c"):
    c=int(t)
    formula=c/5
    print(f"%.2f C is %.2f Farengeit" % (c,formula ))
else:
    print("Try rerun and type again")


#2. Write a Python program to create a string that is made of an input string’s second and last characters.

m=input("Type a string")

print(m[0], m[len(m)-1], sep=" ")
print (m[-1])


#3. Create a string s1, calculate the sum and average of the digits that appear in this string, ignoring all other characters.


s = input("Type a string:")
l = len(s)
integ = 0
i = 0
while i < l:
    s_int = ''
    a = s[i]
    while '0' <= a <= '9':
        s_int += a
        i += 1
        if i < l:
            a = s[i]
        else:
            break
    i += 1
    if s_int != '':
      integ=integ+ (int(s_int))

print(integ)



#4. Create a string. Replace special symbols in your string with #. Example: input = “&^hwjys*%#” output = “##hwjys###”


import re
my_str = "&^hwjys*%#"
my_new_string = re.sub('[^a-zA-Z0-9 \n\.]', '#', my_str)
print(my_new_string)

my_str = "&^hwjys*%#"
k=my_str.replace("^", "#")
print(k)


#5. Create a program that displays your name and complete mailing address formatted in the
# manner that you would usually see it on the outside of an envelope
name= "Yulia"
email="Yulia"+"gmail.com"
print(name, email)

#6. Create two strings and check if all the characters in the string1 are present in string2
# and print the result (True or False)

str1="Hello world!"
str2="Hello"

for t in str2:
    if t in str1[0:len(str1)]:
        print(t , "is in", str1, sep=" ")
        continue

    else:
        print("Some symbols are not in str2")
        break
#7. Create a program that reads the length and width of a farmer’s field from the user.
# Display the area of the field. Hint: The area is 43,5 square km. Use different string formating! (edited)

area=43.5
a=input("type one side")
b=area/float(a)
print(f"Your length is {a} and width is {b}")