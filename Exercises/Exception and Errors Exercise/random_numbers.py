# Get input from user and, based on that input,
# generate and output a random series of numbers between 1 and 500

# import random module
import random

# main function
def main():
    # open the file
    number = open('random.txt', 'w')
    
    # use user input as range value
    for i in range(int(input("How many random numbers should the file hold? "))):     

        #write to the file
        line = str(random.randint(1, 500))
        number.write(line + '\n')

    # close the file outside the loop once it has iterated
    number.close()
     
# call the main function
main()
