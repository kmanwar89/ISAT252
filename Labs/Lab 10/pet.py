# Purpose: A main file used to call the petclass file and instantiate
# a pet object.
# Programmer: Kadar Anwar
# Language: Python 3.4
# pet.py
# 4/20/2015 - ISAT 252

import petclass


def main():
    # User input
    nameinput = input("What is the name of the pet?: ")
    typeinput = input("What type of pet is it? Dog, Bird or Cat?: ")
    ageinput = input("How old is the pet?: ")

    # create a 'pet' object
    userpet = petclass.Pet(nameinput, typeinput, ageinput)

    print("The pet's name is: ", userpet.get_name())
    print("The pet is a: ", userpet.get_type())
    print("The pet is: " + userpet.get_age() + " years old")

main()