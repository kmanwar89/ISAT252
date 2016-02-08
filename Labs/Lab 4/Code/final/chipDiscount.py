# Purpose of Program: A program that computes the discount of chip price
# based on quantity
# Programmer: Kadar Anwar
# Language: Python 3.4
# chipDiscount.py
# 2/20/2015 - ISAT 252

# Declare variables and constants
UNIT_PRICE = 87.00
units = 0.0
PurchasePrice = 0.0
TotalPurchase = 0.0

# Get input from user
units = float(input("Please enter the number of units: "))

# Calculate discount using logic
if units >= 100 and units <=500:
    PurchasePrice = UNIT_PRICE - (UNIT_PRICE * 0.05)
    TotalPurchase = PurchasePrice * units
elif units > 500:
    PurchasePrice = UNIT_PRICE - (UNIT_PRICE * 0.07)
    TotalPurchase = PurchasePrice * units
else:
    TotalPurchase = UNIT_PRICE * units

# Output the result to the customer
print (units, "chips will cost $",format(TotalPurchase, '.2f'))
