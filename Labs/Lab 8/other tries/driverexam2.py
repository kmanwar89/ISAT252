# Purpose: Grade the answers from a drivers' license exam using
# text files, lists and inputs.
# Programmer: Kadar Anwar
# Language: Python 3.4
# driverexam2.py
# 4/2/2015 - ISAT 252

# Main function to call the other functions
def main():
    # Ask the user if they would like to re-initialize the
    # list of correct answers

    answer = None
    while answer != "Yes" and answer != "No":
        answer = input("Would you like to reinitialize the list of \
             correct answers? Please enter Yes or No.")
        if answer != "Yes" and answer != "No":
            print("Please choose either Yes or No")
        else:
            break

    if answer == 'Yes':
        correctanswers()


# Generate a list of the correct answers and write
# them to a text file
def correctanswers():
    answers = ['A', 'C', 'A', 'A', 'D',
               'B', 'C', 'A', 'A', 'C',
               'B', 'A', 'D', 'C', 'D',
               'C', 'B', 'B', 'B', 'D',
               'A']

    outfile = open('answers2.txt', 'w')

    for item in answers:
        outfile.write(item + '\n')

    outfile.close()

correctanswers()

# Prompt the student for a list of answers and write
# them to a text file
def studentanswers():
    # create an empty list
    studentanswers = []

    counter = 0
    # open the file to write
    outfile = open('StudentAnswers.txt', 'w')

    # use a loop to get the values
    while counter != 5:
        answer = input("Enter your answers: ")
        studentanswers.append(answer)
        counter += 1
    # write the values from the list into the
    # text document with a newline appended
    for item in studentanswers:
        outfile.write(item + '\n')

studentanswers()


# Compare the correct answers with the student
# answers, perform analyses and display
# the results
def compare():
    counter = 0
    infile = open('answers2.txt', 'r')
    infile2 = open('StudentAnswers.txt', 'r')

    correct = infile.readline()
    student = infile2.readline()

    while counter != 5:
        if

        else:

        counter += 1
compare()

