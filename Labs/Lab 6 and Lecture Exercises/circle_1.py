# Compute area of a circle
# Programmer:  Kadar Anwar
# Language: Python 3.4
# circle.py
# 3/4/2015 - ISAT 252

#create and initialize global variables and constants
radius = 0.0
area = 0.0
PI = 3.14

#input - get the radius of the circle
radius = float(input("Enter the radius of the circle: "))

#input validation to ensure a proper value
while radius <= 0:
	print("You cannot enter a 0 radius. Please try a different value")
	radius = float(input("Enter the radius of the circle: "))
	               
#process – compute the area of the circle 
area = (radius**2) * PI

#output -display the result
print("The area of the circle is", format(area, '.2f'))
