# Purpose of Program:  Convert Celsius to Fahrenheit
# Programmer: Kadar Anwar
# Language: Python 3.4
# Celsius.py
# 2/9/2015 - ISAT 252

# Create and initialize variables and constants
tempF = 0.0
tempC = 0.0

# Input - gather temperature in Celsius
tempC = float(input("Enter a temperature in Celsius: "))

# Process - calculate and display the temperature in Fahrenheit
tempF = (9/5 * tempC) + 32

# Output - display the converted temperature to the user
print (tempC, "degrees Celsius is", tempF, "degrees Fahrenheit")

