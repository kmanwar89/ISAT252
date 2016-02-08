# Purpose: A program that identifies if a number is positive, negative or zero
# Programmer: Kadar Anwar
# Language: Python 3.4
# number.py
# 2/22/2015 - ISAT 252

# Declare and initialize variables and constants
num = 0.0

# Get input from user
num = float(input("Number?: "))

# Identify if number is positive, negative or zero and output the result
# to the user
if num < 0:
    print ("Negative number")
elif num == 0:
    print ("Zero")
else:
    print ("Positive number")

