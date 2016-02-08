# Purpose: Use and manipulate dictionaries to reinforce the concept
# between keys and values in a dictionary
# Programmer: Kadar Anwar
# Language: Python 3.4
# dictionary.py
# 4/8/2015 - ISAT 252

def main(): 
    roomdict = {'CS101':'3004', 'CS102':'4501', 'CS103':'6755',
                  'NT110':'1244', 'CM241':'1411'}
    profdict = {'CS101':'Haynes', 'CS102':'Alvarado', 'CS103':'Rich',
                  'NT110':'Burke', 'CM241':'Lee'}
    timedict = {'CS101':'8:00AM', 'CS102':'9:00AM', 'CS103':'10:00AM',
                  'NT110':'11:00AM', 'CM241':'1:00PM'}

    # Prompt the user
    userinput = input("Enter a course name for more information: ")

    # Print out the results
    print("The room number is: ", roomdict.get(userinput, "Sorry, that value was not found"))
    print("The professor is: ", profdict.get(userinput, "Sorry, that value was not found"))
    print("The course meets at: ", timedict.get(userinput, "Sorry, that value was not found"))

main()
