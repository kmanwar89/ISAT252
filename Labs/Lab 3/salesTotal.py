# Purpose of Program:  Calculate the sub total, sales tax, and total amount
# of a purchase of 5 items
# Programmer: Kadar Anwar
# Language: Python 3.4
# salesTotal.py
# 2/9/2015 - ISAT 252

# Create and initialize variables and constants
TAX = 0.06
item1 = 0.0
item2 = 0.0
item3 = 0.0
item4 = 0.0
item5 = 0.0
subtotal = 0.0
total = 0.0

# Input - gather price of each item in US dollars
item1 = float(input ("How much does the first item cost (in US dollars?) "))
item2 = float(input ("How much does the second item cost (in US dollars?) "))
item3 = float(input ("How much does the third item cost (in US dollars?) "))
item4 = float(input ("How much does the fourth item cost (in US dollars?) "))
item5 = float(input ("How much does the fifth item cost (in US dollars?) "))

# Process - calculate and display the subtotal of the sale
subtotal = item1 + item2 + item3 + item4 + item5
total = (subtotal * TAX) + subtotal

# Output - display the output to the user, formatted to two decimal places
print("The subtotal of your purchase is $", format(subtotal, '.2f'), \
      "and the total is $", format(total, '.2f'))
