# Purpose of Program:  Calculate the area of a circle
# Programmer: Kadar Anwar
# Language: Python 3.4
# circle.py

# Create and initialize variables and constants
radius = 0.0
area = 0.0
PI = 3.14

# Input - get the radius of the circle
radius = float(input("Input the radius of the circle, in inches: "))

# Process - compute the area of the circle
area = PI * (radius ** 2)

# Ouptut - display the result
print("The area of the circle with radius", radius, "is", area, "inches squared")
