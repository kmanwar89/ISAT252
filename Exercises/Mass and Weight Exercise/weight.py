# Purpose of Program:  Given an objects' mass kg, calculate its weight in Newtons
# and decide if the objects' weight is within given limits.
# Programmer: Kadar Anwar
# Language: Python 3.4
# weight.py
# 2/13/2015 - ISAT 252

# Create and initialize variables and constants
mass = 0.0
weight = 0.0
GRAVITY = 9.8
WEIGHTMAX = 500
WEIGHTMIN = 100

# Input - gather mass of object, in kilograms
mass = float(input("What is the objects' mass, in kg? "))

# Process - calculate the objects' weight in Newtons
weight = mass * GRAVITY

# Output - display the weight of the object, in Newtons, formatted
# to two decimal places.
print ("The objects' weight is", \
       format(weight, '.2f'), "Newtons")

# Decide if object is within acceptable range and output
# a relevant message
if weight > WEIGHTMAX:
	print("The objects' weight is too heavy")
elif weight < WEIGHTMIN:
	print("The objects' weight is too light")
else:
        print("The objects' weight is in an acceptable range")

