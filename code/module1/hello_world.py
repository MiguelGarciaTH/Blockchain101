#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a small example to introduce python language.
- Variable declaration
- If conditions
- For / While loops
- Function defenition
- Class/Object definition
"""


one = 1
two = 2
three = one + two
print(three)

one, two = 1 , 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# Python don't have strong types, but is typed on assigment
one = 1
two = 2
hello = "hello"

#print(one + two + hello) # This do not work


mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print(x)

mylist = [1,2,3]
print(mylist[2])

helloworld = "hello" + " " + "world"
print(helloworld)


# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)


# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))


## STRINGS
astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))

astring = "Hello world!"
print(astring.index("o"))

astring = "Hello world!"
print(astring.count("l"))

astring = "Hello world!"
print(astring[3:7])

astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

## conditions
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")
