# Introduction to Programming Languages using Python
# All course codes

# Basic Calculations
print (2 + 3)
print (20 / 3)

# Variables
# Naming Variables
userAge = 50
userName = ("Mohamed")
print (userAge)
print (userName)

# Basic Operators
print (10 - 3)              # Substruction
print (10 + 3)              # Addition
print (10 * 3)              # Multiplication
print (10 / 3)              # Division
print (10 // 3)             # Floor Division
print (10 ** 3)             # Power
print (10 % 3)              # Modulus

# Python uses BODMAS
print (20 + 8 / 5 * 4 - 7)

# More Assignment Operators
x = 6
print (x)

x = x + 4
print (x)

x += 7
print (x)

x -= 7
print (x)

x*= 7
print (x)

x /= 7
print (x)

x //= 7
print (x)

x **= 7
print (x)

x %= 7
print (x)

y = 50
print (y)

z = 18
print (z)

z *= 2
print (z)

# Data Types in Python
# Integer = Whole Numbers
userPhone = 565
print (userPhone)

n1 = 76
n2 = 90
print (n1 * n2)

# Float = Decimals
userSalary = 1234.5
print (userSalary)

n3 = 9.5
n4 = 1.2
print (n3 + n4)


# String = Text
userName = "ali"
print (userName)

#Built-in-Functions in String
userName2 = "ahmed"
print (userName2.upper())

userName3 = "AHMED"
print (userName3.lower())


# String formating using concatenation 
firstName = "Abdi "
lastName = "Ahmed"
print (firstName + lastName)


# String formating using % operator
Car = "Mark II"
Price = 3000
excRate = 35.5

message = "The price of  %s car is %d dollars and the exchage rate of  USD to SOS is %4.2f " % (Car, Price, excRate)
print (message)


# String formating using the format() method
Phone = "Samsung"
Price = 1500
exRate = 37.5

message1 = "The price of {0:s} phone is {1:d} and the exchage rate of USD to SOS is {2:4.2f}".format(Phone, Price, exRate)
print (message1)

message2 = "{0:s} is better than {1:s}".format("Python", "Java")
print (message2)


# Type Casting (Conversion between Data Types)
int (2.2)           # From float to integer
float (2)           # From integer to float
str (2)             # From integer to string
str (2.2)           # From float to string
float ('2')         # From string to float

# Advanced Data Types (Lists, Tuples & Dictionaries)
# Lists
# Lists are Modifiable

# Declaring a List
myGrades = [60, 55, 80, 95, 33, 71, 45]

# Printing the entire List
myGrades
print (myGrades)

# Indexing a List
myGrades [1]
myGrades [5]

# Assigning a List
myGrades1 = myGrades
myGrades1

# Slicing a List
myGrades [2:4]

# Slicing a List with stepper
myGrades [3:5:2]

# Slicing a List (default)
myGrades [ :3]
myGrades [2: ]

# Modifiying a List
myGrades [2] = 90

# Adding items to the List
myGrades.append(25)

# Find the number of items in a List
print (len(myGrades))

# Deleting or removing items in the List
del myGrades [3]

# Deleting the whole List
del myGrades

# Tuples
# Tuples are Unmodifiable 
# Declaring a Tuple
mySavings = (230, 340, 56, 113)
print (mySavings)

# Indexing a Tuple
mySavings [2]

# Check if an item in a Tuple
340 in mySavings

# Find the number of items in a Tuple
print (len(mySavings))

# Concatinating Tuples
print (mySavings + (80, 44)
print (mySavings)

# Duplicating a Tuple
print (mySavings)
print (mySavings*5)

# Deleting a Tuple
print (mySavings)
del mySavings
print (mySavings)

# Dictioneries
# Dictionary is a collection of related data pairs.
# Dictioneries are Modifiable

# Declaring a dictionary
myDict = {"Abdi" : 20, "Mohamed" : 30}
print (myDict)

# Declaring a dictionary using the dict() method
myDict1 = dict (Ali = 50, Amal = 60)
print (myDict1)

# Accessing a dictionary
print (myDict["Mohamed"])

# Modifying a dictionary
myDict["Mohamed"] = 10

# Declaring empty dictionary
emptyDict = {}
print (emptyDict)

# Adding items to a dictionary
myDict["Adam"] = 90
print(myDict)

# Removing item from a dictionary
del myDict["Adam"]
print (myDict)

# Deleting an entire dictionary
del myDict

# Making Your Program Intractive
# Python's Built-In Functions: Input(), and Print()

myName = input("Please enter your name: ")
myAge = input("Please enter your age: ")
print ("Hello There! my name is", myName, "and I am", myAge, "years old")

# Printing my program using % formatter
print ("Hello There! my name is %s and I am %s years old" % (myName, myAge))

# Printing my program using format() method
print("Hello There! my name is {} and I am {} years old".format(myName, myAge))

# Triple Quotes
# Printing a long statement
print(''' Hello there!
my name is Ali and I am 33 years old,
and I work as engineer ''')

# Escaping Characters Using Backslash \
# Printing a Tab
print("Hi \tThere")

# Printing a New Line
print("Hi \nThere")

# Printing the Backlash itself
print("\\")

# Printing the Entire String without Looking after the Backlash
print(r"Hi \tThere")

# Making Decisions and Choices
# Condition Statements
# The Result would a Boolean either True or False

# Equal (==)
print(3 == 5)
print(3 == 3)

# Not Equal (!=)
print(3 != 4)

# Greater Than (>)
print(5 > 3)
print(3 > 5)

# Less Than (<)
print(3 < 8)
print(3 < 0)

# Greather Than or Equal
print(3 >= 5)
print(5 >= 3)

# Less Than or Equal
print(6 <= 5)
print(5 <= 6)

# Logical Operators
# AND, OR, Not

# AND
print(3 == 3 and 4 > 5)

# OR
print(2 < 0 or 4 < 7)

# Not
print(not 3 > 9)
print(not 4 == 4)
