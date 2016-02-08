# Purpose: Use lists and file IO to gather answers
# for grading a drivers license exam. Use string comparison
# and input validation to find the right answer and display the
# results to the end user.
# Programmer: Kadar Anwar
# Language: Python 3.4
# driverexam.py
# Submitted 4/8/2015 - ISAT 252

def main():
    # initialize the answers array
    answers = ['A', 'C', 'A', 'A', 'D'
               'B', 'C', 'A', 'A', 'C',
               'B', 'A', 'D', 'C', 'D',
               'C', 'B', 'B', 'B', 'D',
               'A']
    wronganswers = []

    # Get answers from the student, put them into a text file
    studentanswers()

    # Read answers from student answers file
    try:
        userfile = open('StudentAnswers.txt', 'r')
        student = userfile.read().splitlines()
        userfile.close()
    except IOError:
        print("File does not exist")

    # error handling and comparison between correct answer and
    # provided answer
        counter = 0
        correct = 0
        incorrect = 0
        questions = 20

        # print a neat header
        print("Q\tCorr\tYour")
        print("#\tAnswer\tAnswer\n----------------------")

        # compare between correct and provided answer
        while counter != 20:
            # format the output
            print(str(counter+1) + "\t" + answers[counter] + "\t\t" + student[counter])  # ,end="\t" ), if necessary
            if student[counter].strip() == answers[counter].strip():
                counter += 1
                correct += 1
                print("\t\t\tCorrect")
            else:
                wronganswers.append(counter)
                incorrect += 1
                counter += 1
                print("\t\t\tIncorrect")

        # print an output to the user informing them of the results
        perc_correct = (correct/questions) * 100
        if perc_correct < 75:
            print("A passing score is 75%. Your score was " + str(perc_correct) + "%. You did not pass")
        else:
            print("Your score was " + str(perc_correct) + "%. You passed the exam!"
                  " Congrats!")

        print("Answers correct: ", correct)
        print("Answers incorrect: ", (questions - correct))
        print("The incorrect answers were: ", wronganswers)


def studentanswers():
    # Prompt the student for a list of answers and write
    # them to a text file

    # create an empty list
    studentanswers = []
    counter = 0
    choices = ['A', 'B', 'C', 'D']

    # open the file to write
    outfile = open('StudentAnswers.txt', 'w')

    # use a loop to get the values
    # input validation
    while counter != 20:
        answer = input("Enter your answers: ")
        answer = answer.upper()
        if answer in choices:
            counter += 1
            studentanswers.append(answer)
        else:
            print("That is not a valid answer")

    # write the values from the list into the
    # text document with a newline appended
    for item in studentanswers:
        outfile.write(item + '\n')

    # close the file
    outfile.close()

main()
