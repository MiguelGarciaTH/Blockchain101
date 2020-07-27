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

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass


x = [1,2,3]
y = [1,2,3] # y = x
print(x == y) # Prints out True
print(x is y) # Prints out False


## FOR loops
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)


## Dictionaries
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)


phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)


phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))


phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
del phonebook["John"]
print(phonebook)

phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
phonebook.pop("John")
print(phonebook)

## NUMPY ARRAYS
# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

# Calculate bmi
bmi = np_weight / np_height ** 2

# Print the result
print(bmi)

# For a boolean response
print(bmi > 23)

# Print only those observations above 23
print(bmi[bmi > 23])

for i in (range(24, -1, -8)*2):
    print(i)
