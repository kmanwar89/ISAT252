
def main():
    # initialize the answers array
    answers = ['A', 'C', 'A', 'A', 'D',
               'B', 'C', 'A', 'A', 'C',
               'B', 'A', 'D', 'C', 'D',
               'C', 'B', 'B', 'B', 'D',
               'A']

    # Get answers from the student, put them into a text file
    studentanswers()

    # # Read answers from correct answers file
    # rightfile = open('answers.txt', 'r')
    # answers = rightfile.read().splitlines()
    # rightfile.close()
    # print("Correct answers: ", answers)

    # Read answers from student answers file
    userfile = open('StudentAnswers.txt', 'r')
    student = userfile.read().splitlines()
    userfile.close()
    print("Your answers: ", student)

    try:
        counter = 0
        correct = 0
        incorrect = 0
        questions = 20
        total = 0

        while counter != 20:
            if student[counter].strip() == answers[counter].strip():
                correct += 1
                counter += 1
            else:
                incorrect += 1
                counter += 1

        print("# Correct: ", correct)
        print("# Incorrect: ", (questions - correct))

        # print("Correct avg:", (correct/len(student)))
        # print("Incorrect avg:", (incorrect/questions))

    except ValueError as err:
        print("Some ValueError occurred. Error is: ", err)
    except IOError as err:
        print("File not found. Error is: ", err)























# Prompt the student for a list of answers and write
# them to a text file
def studentanswers():
    # create an empty list
    studentanswers = []

    counter = 0
    # open the file to write
    outfile = open('StudentAnswers.txt', 'w')

    # use a loop to get the values
    while counter != 20:
        answer = input("Enter your answers: ")
        answer = answer.upper()
        studentanswers.append(answer)
        counter += 1
    # write the values from the list into the
    # text document with a newline appended
    for item in studentanswers:
        outfile.write(item + '\n')

main()
