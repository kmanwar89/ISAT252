# Purpose: Ask the user to enter grades and, using a list, perform calculations
# on the entered values.
# Programmer: Kadar Anwar
# Language: Python 3.4
# numAnalysis
# 4/1/2015 - ISAT 252


def analyze():
    # initialize an empty list
    num = [0]*20
    counter = 20

    # loop through asking user for 20 values
    # start the counter at 20 in this case
    while counter != 0:
        # use an
        try:
            # have the user input a value
            score = int(input("Please enter" + " " + str(counter) + " " + "more value(s): "))
            # decrement the counter
            counter -= 1
            # add the inputted value to the num[] list
            num.append(score)
        except ValueError:
                print("Please enter a whole number")

    # loop through the num list
    for score in num:
        total = 0.0
        counter = 0
        total += score
        counter += 1

    # output the results of the analysis
    low = min(num)
    print("Lowest number is:", low)
    high = max(num)
    print("Highest number is:", high)
    total = sum(num)
    print("The total of the values is:", total)
    avg = (sum(num)/len(num))
    print("Average is:", avg)

# call the above function
analyze()
