# Chapter 3 challenges

# print 3 different strings
for i in range(3):
    print(f"this is string number {i + 1}")

""" write a program that prints a message if varibale is less than 10,
    or different message if greater than 10 """
number = 6
if number < 10:
    print(f"{number} is less than 10")
else:
    print(f"{number} is greater than 10")
number = 12
if number < 10:
    print(f"{number} is less than 10")
else:
    print(f"{number} is greater than 10")

""" write a program that prints a message if variable is less than 10,
    another message if greater than 10, but less than 25,
    and another message if greater than 25 """
number = 17
if number < 10:
    print(f"{number} is less than 10")
elif number < 25:
    print(f"{number} is greater than 10 and less than 25")
else:
    print(f"{number} is greater than 25")

# create a program than divides 2 varaibles and prints the remainder
num1 = 10
num2 = 3
remainder = num1 % num2
print(f"the remainder of {num1} divided by {num2} is {remainder}")

# create a program that divides 2 numbers and prints the quotient
num1 = 10
num2 = 3
quotient = num1 // num2
print(f"the quotient of {num1} divided by {num2} is {quotient}")

""" write a program with 'age' assigned to an integer,
    that prints different strings depending on what value 'age' is"""

def check_age(age):
    if age <= 12:
        print(f"{age} is the age of a child")
    elif age <= 21:
        print(f"{age} is the age of a teen")
    elif age <= 60:
        print(f"{age} is the age of an adult")
    elif age <= 101:
        print(f"{age} is the age of an old person")
    else:
        print(f"{age} is the age of someone who's probably dead")

age = 12
check_age(age)
age *= 2
check_age(age)
age *= 2
check_age(age)
age *= 2
check_age(age)
age *= 2
check_age(age)
