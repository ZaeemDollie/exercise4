# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
  
list_of_fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# TODO: Use a for loop to print each fruit in the list

for fruit in list_of_fruits:
    print(fruit)
#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
countdown = 5

while countdown > 0:
    print(countdown)
    countdown -= 1

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers

for i in range(1, 11):
    print(i**2)
#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module

import time

time.sleep(3)
print("Hello World")

# TODO: Create a list of colors

list_of_colors = ["blue", "black", "red", "yellow", "green", "purple"]

# TODO: Use a for loop to select and print 3 random colors from the list

import random
for i in range(3):
    random_color = random.choice(list_of_colors)
    print(random_color)
#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions


# TODO: Use a while loop to create a simple calculator
