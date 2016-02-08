# Purpose: Solve a quadratic formula given a, b and c
# Programmer: Kadar Anwar
# Language: Python 3.4
# quadratic.py
# 2/20/2015 - ISAT 252

# Import the math module
import math
import sys

# Declare and initialize variables and constants
a, b, c = 0.0, 0.0, 0.0
discrim = 0.0
discRoot = 0.0
quotient = 0.0
root1, root2 = 0.0, 0.0

# Get input from user
a = float(input("\nPlease enter the value of a: "))
b = float(input("\nPlease enter the value of b: "))
c = float(input("\nPlease enter the value of c: "))

# Calculate the discriminant
discrim = ((b**2) - (4*a*c))

# Calculate the value of -b / 2*a
quotient = (-b / (2*a))

# check value of 'a' to make sure it isn't invalid
if a==0:
    print ("The value of a cannot be equal to zero.  Program will " \
              "not continue")
    sys.exit()
    
# Solve the equation based on value of discriminant
if discrim < 0:
    discRoot = math.sqrt((-1 * discrim))
    print("The roots are: " + str(quotient) + "+i and " + str(quotient) + "-i")
elif discrim == 0:
    root1 = -b / (2*a)
    root2 = -b / (2*a)
    print ("The roots are: " + format(root1, '.2f') + " and " + \
        format(root2, '.2f'))
else:
    root1 = (-b + math.sqrt(discrim)) / 2*a
    root2 = (-b - math.sqrt(discrim)) / 2*a
    print ("The roots are:" + " " + format(root1, '.2f') + " and " + \
        format(root2, '.2f'))
