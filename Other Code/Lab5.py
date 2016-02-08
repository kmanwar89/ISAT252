# Purpose: Calculate Average Rainfall over a period of time
# Programmer: Kadar Anwar
# Language: Python 3.4
# rainfall.py
# 2/28/2015 - ISAT 252

# Declare variables and constants
years = 0.0
rainfallMonth = 0.0
months = years * 12
totalRain = 0.0
averageRain = 0.0
m = 0

# Get input from user
for m in range(0,13,1):
    rainfallMonth = float(input("Enter the rainfall for the month"))
    m += 1

# Output
print()
print(m)
    
# Output the result to the user
