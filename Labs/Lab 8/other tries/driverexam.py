# Purpose: Grade the answers from a drivers' license exam using
# text files, lists and inputs.
# Programmer: Kadar Anwar
# Language: Python 3.4
# driverexam.py
# 4/2/2015 - ISAT 252


def answers():
    # Create a list of correct answers to compare against
    answers = ['A', 'C', 'A', 'A', 'D',
               'B', 'C', 'A', 'A', 'C',
               'B', 'A', 'D', 'C', 'D',
               'C', 'B', 'B', 'B', 'D',
               'A']

    # Open a file for writing
    outfile = open('answers.txt', 'w')

    # Write the list to the file.
    for item in answers:
        outfile.write(item + '\n')

    # Close the file
    outfile.close()

# Call the function
answers()

def studentAnswers():
    # local constants
    QUESTIONS = 20

    # open the answers file
    file = open("answers.txt", "r")

    # initialize an empty list
    student = [0] * QUESTIONS
    counter = 20

    # loop through asking user for 20 values
    # start the counter at 20 in this case
    while counter != 0:
        # have the user input a value
        answer = int(input("Please enter your answer for question" + " " + str(counter) + ":"))
        # decrement the counter
        counter -= 1
        # add the inputted value to the student[] list
        student.append(answer)

    # loop through the num list
    # for score in num:
    #     total = 0.0
    #     counter = 0
    #     total += score
    #     counter += 1


# call the function
studentAnswers()


def compare():
