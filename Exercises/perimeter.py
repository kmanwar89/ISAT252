#Purpose of Program - calculate perimeter of a rectangle
#Programmer: Kadar Anwar
#Language: Python 3.4.2
#perimeter.py
#2/9/2015 - ISAT 252

# tell the user what we're going to do before gathering input
print ("Let's calculate the perimeter of a rectangle")

# declare variables
length = 0.0
width = 0.0
perimeter = 0.0

# Input - get the length
length = float(input("What is the length of the rectangle? "))

# Input - get the width
width = float(input("What is the width of the rectangle? "))

# Process - perform the calculation of the perimeter
perimeter = (2*length) + (2*width)

# Output - display the result
print ("The perimeter of a rectangle with length", length, "and width", width, "is", perimeter)
