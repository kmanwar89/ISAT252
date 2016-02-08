# Purpose: Grade the answers from a drivers' license exam using
# text files, lists and inputs.
# Programmer: Kadar Anwar
# Language: Python 3.4
# driverexam2.py
# 4/2/2015 - ISAT 252


def main():
    answers = ['A', 'C', 'A', 'A', 'D',
               'B', 'C', 'A', 'A', 'C',
               'B', 'A', 'D', 'C', 'D',
               'C', 'B', 'B', 'B', 'D',
               'A']

    studentanswers = []
    incorrectlist = []
    correct = 0
    incorrect = 0
    questions = 20
    counter = 20

    # Read each line from the StudentAnswers.txt file
    # and put it into the studentanswers[] list
    infile = open('StudentAnswers.txt', 'r')
    studentanswers = infile.readlines()
    infile.close()

    infile2 = open('answers.txt', 'r')
    correctanswers = infile2.readlines()
    infile2.close()

    try:
        while counter < 20:
            if studentanswers[counter].strip() == correctanswers[counter]:
                correct += 1
                counter += 1
                print("\t\tCorrect")
                print("# correct: ", correct)
            else:
                incorrect += 1
                counter += 1
                print("\t\tIncorrect")
                print("# incorrect: ", incorrect)
    except ValueError:
        print("Incorrect value somewhere in program")
    except IOError:
        print("The file was not found. Please place the text file with \
        the answers in the same folder as the python file")






# # Analysis of results
# correctavg = correct / len(answers)
# correctpercent = (correct/questions) * 100
# incorrectavg = incorrect/ len(studentanswers)
# print("Average Correct: ", correctavg)
# print("Average Incorrect: ", incorrectavg)
# if correctpercent >= 75:
#     print("Your score was: " + str(correctpercent) + ". You pass!")
# else:
#     print("Your score was: " + str(incorrectavg) + ". You fail!")


# # BONUS POINTS
# # Prompt the student for a list of answers and write
# # them to a text file
# def studentanswers():
#     # create an empty list
#     studentanswers = []
#
#     counter = 0
#     # open the file to write
#     outfile = open('StudentAnswers.txt', 'w')
#
#     # use a loop to get the values
#     while counter != 5:
#         answer = input("Enter your answers: ")
#         studentanswers.append(answer)
#         counter += 1
#     # write the values from the list into the
#     # text document with a newline appended
#     for item in studentanswers:
#         outfile.write(item + '\n')
# studentanswers()

main()
