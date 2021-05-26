# COM 112 Course : Intro to Programming Languages (using Python)
# Taught by Mr. Abdullahi Cadceed, Dean of the Faculty of Information Science & Technology, East Africa University Qardho
# All course codes wil be available in here

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

# Deleting or removing items to the List
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

