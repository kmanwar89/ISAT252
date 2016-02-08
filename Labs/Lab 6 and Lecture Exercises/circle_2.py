# Compute area of circle using two functions
# Programmer:  Kadar Anwar
# Language: Python 3.4
# circle_2.py
# 3/4/2015 - ISAT 252

#define the main function and get the input of the radius
def main():
    radius = float(input("Enter the radius of the circle: "))
	
	#input validation to ensure a proper value
    while radius <=0:
        radius = print("Please enter a value greater than 0")
        radius = float(input("Enter the radius of the circle: "))    
		
    compute_area(radius) # pass the radius value as an argument to the compute_area function

# define the compute_area function and local variables, and compute
# the area of a circle using the function.
def compute_area(number):
    PI = 3.14
    area = 0.0
    area = (number**2) * PI
    print("The area of the circle is", format(area, '.2f'))
    
# Call the main function to output the result to the user
main()


