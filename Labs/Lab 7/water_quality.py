# Purpose: Calculate the average pH or Turbidity given data in a text file
# Programmer: Kadar Anwar
# Language: Python 3.4
# water_quality.py
# 3/23/2015 - ISAT 252

def main():
    # Present a menu to the user
    print("Friends of the Shenandoah: Water Quality Data")
    print("---------------------------------------------")
    print("Select one of the following options: ")
    print("1: Open LabpH.txt")
    print("2: Open Turbidity.txt")

    # Input validation
    choice = None

    while choice != "1" and choice != "2":
        choice = input("Which file do you want to open? ")
        if choice != "1" and choice != "2":
            print("Please pick 1 or 2")
        else:
            break

    # Assign filename to a variable based on users' choice
    filename = None

    if choice == "1":
        filename = "LabpH.txt"
    elif choice == "2":
        filename = "Turbidity.txt"

    # Call the calculate_average function and pass it the
    # filename of choice.
    calculate_average(filename)

# Define a function to calculate the average value
def calculate_average(filename):
    total = 0.0
    counter = 0.0
    
    # open the file as read-only
    file = open(filename, 'r')

    # capture the file header and remove extra spaces
    header = file.readline()
    header = header.strip()

    # use a loop to iterate through the file and sum the values
    for line in file:
        amount = float(line)
        total += amount
        counter += 1

    # calculate the average and format the result
    average = (total / counter)
    average = format(average, '.2f')

    # display the result in human-readable format
    print("Average", header + ": " + average)

    # close the file
    file.close()

# return control to main()
main()
