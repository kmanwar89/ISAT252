# Purpose: Calculate number of dollars based on leftover change
# Programmer: Kadar Anwar
# Language: Python 3.4
# change.py
# 2/22/2015 - ISAT 252

# Declare variables and constants
change = 0.0
dollars = 0.0

# Get input from user
change = float(input("Enter the change: "))

# Calculate change and output the result to the user
dollars = int((change / 100))
print (dollars)

if change >= 100:
    print("Your change contains", dollars, "dollars.")
    #print("Your change contains " + \ # this output doesn't work right?
    #      format(dollars, '.2f') + " dollars")
else:
    print ("Your change contains no dollars.")
    
# Output the result to the user
