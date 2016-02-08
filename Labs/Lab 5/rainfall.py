# Calculate average rainfall over a period of years
# Kadar Anwar
# Python 3.4
# rainfall.py
# 2/27/2015 - ISAT 252

# Import system library
import sys

# Initialize variables and constants
years = 0
totalRain = 0.0
rainMonth = 0.0
monthAverage = 0.0
yearAverage = 0.0

# Ask user for number of years of data to calculate
years = int(input("Enter the number of years (whole number): "))

# Make sure the user doesn't enter an invalid number of years and
# perform relevant calculations
if years <= 0:
    print("Please enter a value greater than 0!")
    sys.exit() # exit the program if years entered is = 0.
elif years >0:    
    for i in range(years):
        for j in range(0,12):
            rainMonth = float(input("Inches of rainfall?: "))
            totalRain = totalRain + rainMonth

# Calculate average values
monthAverage = totalRain/((years*12))
yearAverage = totalRain/years

# Output formatted results to user
print("Total Rainfall:", format(totalRain, '.2f'), "inches")
print("Average Rainfall per month:", format(monthAverage, '.2f'), "inches")
print("Average Rainfall per year:", format(yearAverage, '.2f'), "inches")

