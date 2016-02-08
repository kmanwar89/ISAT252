# Predict approximate size of a population of organisms
# Kadar Anwar
# Python 3.4
# population.py
# 3/1/2015

# Initialize and declare variables and constants
startOrg = 0.0 # starting number of organisms
popIncrease = 0.0 # population increase percent
numDays = 0 # numberof days to increase population
endOrg = 0.0 # ending number of organisms
days = 1 # used to display the day in the final table

# Ask user for starting values
startOrg = float(input("Input the starting number of organisms: "))

# Check for invalid values
while startOrg <= 0:
    print("Please input a value greater than 0!")
    startOrg = float(input("Input the starting number of organisms: "))
    
# Enter remaining values
popIncrease = float(input("Please enter the population percent increase: "))
popIncrease = popIncrease / 100
numDays = int(input("Please enter the number of days to multiply (whole number): "))
print(" ")

# Format table heading
print("Day \t\t Approx. Population")
print("-------------------------")

# Perform a calculation and output the result in a table
for i in range(1, numDays):
    endOrg += (startOrg * popIncrease) + startOrg
    numDays += 1
    print(days, '\t\t', format(endOrg, '.2f'))
    days += 1
    print()
