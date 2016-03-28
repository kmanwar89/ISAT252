# Purpose: This program uses a function to calculate the
# total of the values in a list.
# Programmer: Kadar Anwar
# Language: Python 3.4
# ListTotals.py
# 3/28/2016 - ISAT 252

# Define main()
def main():
    
    #Create a list
    numbers = [2,4,6,8,10]

    # Display the total of the list elements by calling the
    # appropriate function
    print('The total is', get_total(numbers))
    print('The average is', get_average(numbers))
    

# The get_total value function iterates over a list, sums the values
# and returns the sum

def get_total(value_list):
    total = 0

    for num in value_list:
        total += num

    return total

# The get_average function iterates over a list, sums the values, calculates
# the average and returns the average using the length of the list
# to calculate the average
def get_average(value_list):
    average = 0.0
    total = 0.0
    
    for num in value_list:
        total += num
        average = total/len(value_list)
        
    return average

# Call the main() function
main()
