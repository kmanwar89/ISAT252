# Purpose of Program:  Calculate the miles-per-gallon of a vehicle
# Programmer: Kadar Anwar
# Language: Python 3.4
# mpg.py
# 2/9/2015 - ISAT 252

# Create and initialize variables and constants
mpg = 0.0
miles = 0.0
gallons = 0.0

# Input - gather number of miles driven and gallons of gas used
miles = float(input("How many miles did you drive? "))
gallons = float(input("How many gallons did you use? "))

# Process - calculate the vehicles' miles per gallon
mpg = miles / gallons

# Output - display the calculated miles per gallon result to the user, 
# formatted to two decimal places
print ("Your vehicles' miles per gallon is", \
       format(mpg, '.2f'), "miles per gallon")

