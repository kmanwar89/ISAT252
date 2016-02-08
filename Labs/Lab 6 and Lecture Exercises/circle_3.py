# Compute area and circumference of a circle utilizing functions
# Programmer:  Kadar Anwar
# Language: Python 3.4
# circle_3.py
# 3/4/2015 - ISAT 252

# Create and initialize variables and constants
PI = 3.14

# Define the main function and get the input of the radius
def main():
    # define variables and constants
    area = 0.0
    circum = 0.0

    # get the input from the user and ensure a valid value is used
    radius = float(input("Enter the radius of the circle: "))

    while radius <= 0:
        print("Please enter a valid value greater than 0.")
        radius = float(input("Enter the radius of the circle: "))
    
    # pass radius value to two different functions
    area=compute_area(radius)
    circum=compute_circumference(radius)
    
    # output the formatted results to the user
    print("The area of the circle is", format(area, '.2f'))
    print("The circumference of the circle is", format(circum, '.2f'))
    
def compute_area(number):
    # define variables and constants
    area = 0.0

    # calculate area
    area = PI * (number**2)

    # return value to main function
    return area

def compute_circumference(number):
    # define variables and constants
    circum = 0.0

    # calculate circumference
    circum = (2 * PI * number)

    # return value to main function
    return circum
    
# Call the main function to output the result to the user
main()


