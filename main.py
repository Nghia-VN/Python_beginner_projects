"""print("Hello World!")
first_name = "Van Nghia Do"
print(f"Hello {first_name}")
# variable String
object = "Math"
print(f"I like {object} and i'm {first_name}")
# variable Integers
age = 25
print(f"And I'm {age} years old")
# Float
GPA = 2.48
print(f"my GPA is {GPA}")
# boolean
status = False
if status:
    print(f"I'm Online!")
else:
    print(f"I'm Offline!")
# multi variable
first_name1, last_name = "Van Nghia", "Do"
print(f"my full name is {first_name1} {last_name}")
# typecasting
num = 10
string = "25"
flo = 3.9
is_you = True

string = int(string)
print(type(string))
# input()
name = input("Hi,I'm ")
print(f"My name is: {name}")
age = int(input("how old are u ?:"))
age += 1
print(f"you are {age} years old")
# example
length = int(input("Enter the length:"))
width = int(input("Enter the width:"))
acreage = length * width
print(f"acreage is:{acreage}cm²")"""

# example
"""

item = input("Your Item :")
price = float(input("Price: "))
quantity = int(input("How many Item: "))
total = price * quantity
print(f"{quantity} x {price}")
print(f"total: ${total}")"""
# Madlibs game
"""noun1 = input("Enter a noun (Location): ")
noun2 = input("Enter a noun (Food): ")
adjective = input("Enter an adjective: ")

print(f"today i went to {noun1}")
print(f"in there i eat {noun2}")
print(f"i feel like {adjective}")
"""
import math

"""
radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference is : {round(circumference)}")
"""
# if else
"""
name = input("Enter your name: ")
if name == "":
    print("You can wirte your name!")
else:
    print(f"Created your name is {name}")"""
# calculator program
"""
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2th number: "))
operator = input("Enter a operator: ")
if operator == "+":
    result = num1 + num2
    print(f"resulr: {result}")
elif operator == "-":
    result = num1 - num2
    print(f"resulr: {result}")
elif operator == "*":
    result = num1 * num2

    print(f"resulr: {result}")
elif operator == "/":
    result = num1 / num2

    print(f"resulr: {result}")
else:
    print(f"{operator} is not correct!")"""
# Python weight converter
"""
weight = float(input("Enter your weight:"))
unit = input("Choice Kilograms or Pounds (K or L):")
if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {weight} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kg"
    print(f"Your weight is: {weight} {unit}")
else:
    print(f"{unit} is not valid")"""
# Temperatur program
"""
location = input("Enter your location: ")
unit = input("Choice °C or °F:")
temp = float(input("Enter the Temperatur:"))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperatur in {location} is {temp} °F")
elif unit == "F":
    temp = round((temp - 32) * 1.8, 1)

    print(f"The temperatur in {location} is {temp} °C")
else:
    print("you valid is not correct")"""
# logical operators
"""

temp = int(input("Enter the temperatur:"))
is_raning = True
is_sunny = False

if temp > 30 or temp > 0 and not is_raning and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")
elif temp <= 0 and is_raning and not is_sunny:
    print("It is so COLD outside")
    print("It is SLEET")
elif temp >= 20 and temp < 27 or not is_raning or not is_sunny:
    print("It is WARM outside")
    print("It is CLOUDLY")"""
# conditional expression
"""
temp = int(input("Enter the temparatur:"))
print("Good day" if 23 < temp <= 30 else "Bad day")"""

# string indexing
"""

credit_number = "1234-567-8910"
print(f"XXX-XXX-XXX-{credit_number[-4::]}")"""
# format specifiersi
"""
price1 = 3000.14159
price2 = -9039.1903
price3 = 19203.02

print(f"Price 1 is {price1:+,.2f}")
print(f"Price 2 is {price2:+,.2f}")
print(f"Price 3 is {price3:+,.2f}")
"""

# while loop
"""
name = input("Enter your name:")
age = int(input("Enter your age:"))
while name == "" or age < 18:
    print("You did not enter your name")
    name = input("Enter your name:")
    print("you are not old enough")
print(f"Hallo {name}")"""
# Python compund interest caculator
"""
principle = 0
rate = 0
time = 0
while True:
    principle = float(input("Enter the principle amount:"))
    if principle < 0:
        print("Principle can't be less than zero!")
    else:
        break
while True:
    rate = float(input("Enter the interest rate:"))
    if rate < 0:
        print("Rate can't be less than zero!")
    else:
        break
while True:
    time = float(input("Enter the time in year/s:"))
    if time < 0:
        print("Time can't be less than or equal zero!")
    else:
        break
total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")"""
# for loops
'''
for x in range(2, 18):
    if x == 13:
        continue
    else:
        print(x)
    '''
    # countdown project
import time
my_time = int(input("Enter the time: "))
for x in range(my_time, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
print("Time's up")

