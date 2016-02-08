__author__ = 'kadar'
# Generate a random series of numbers between 1 and 500
import random

def main():
    for count in range(int(input("How many random numbers should the file hold?"))):
        # open the text file
        number = open(random.txt, w)

        #write to the file
        number.write(str(random.randint(1, 500)))

        #close the file
        number.close()

# call the main function
main()
