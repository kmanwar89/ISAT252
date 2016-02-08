# Commuter buddy - calculate yearly CO2 emissions based on distance to work
# and efficiency of the vehicle
# Programmer:  Kadar Anwar
# Language: Python 3.4
# emissions.py
# 3/4/2015 - ISAT 252

# Create and initialize variables and constants
GASEMISSIONS = 19.4 #CO2 emissions for 1 gallon of gas, in pounds/gallon

def main():
    # declare local variables
    distanceToWork = 0.0
    daysWorked = 0.0
    milesPerYear = 0.0
    mpg = 0.0
    gallonsPerYear = 0.0
    emissions = 0.0

    # get user input
    distanceToWork = float(input("What is the distance driven to work? "))
    mpg = float(input("What is your vehicles' mpg? "))
    daysWorked = float(input("How many days per week are worked? "))
        
    # call functions and store results in variables
    milesPerYear = yearly_miles_driven(distanceToWork, daysWorked)
    gallonsPerYear = gallons_used_per_year(milesPerYear, mpg)
    emissions = gas_emission_per_year(gallonsPerYear)

    # output the formatted results in a table
    print("Distance to work \t MPG of vehicle \t Number of days/week \t Emissions for a year")
    print(format(distanceToWork, '.2f'), "miles \t\t", format(mpg, '.2f'), "mpg \t\t", format(daysWorked, '.2f'), '\t\t\t', format(emissions,'.2f'))

    # declare functions and use them to perform calculations
def yearly_miles_driven(distanceToWork, daysWorked):
    milesPerYear = 0.0
    WEEKSINYEAR = 52

    milesPerYear = 2 * (distanceToWork * daysWorked * WEEKSINYEAR)

    return milesPerYear

def gallons_used_per_year(milesPerYear, mpg):
    gallonsUsed = 0.0

    gallonsUsed = (milesPerYear / mpg)
    
    return gallonsUsed

def gas_emission_per_year(gallonsPerYear):
    poundsPerYear = 0.0

    poundsPerYear = GASEMISSIONS * gallonsPerYear

    return poundsPerYear

    # call main function to execute the program
main()
