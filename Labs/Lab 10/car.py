# Purpose: A main file used to instantiate and use a Car object
# and call methods within the carclass class.
# Programmer: Kadar Anwar
# Language: Python 3.4
# car.py
# 4/20/2015 - ISAT 252

import carclass


def main():
    # Error exception for the year
    # to make sure user only enters numbers.
    # count is used as a fake placeholder variable to ensure the loop
    # continues to prompt the user until they enter a valid value.
    count = 0
    while count == 0:
        try:
            year = int(input("What is the car's model year?: "))
            count += 1
        except ValueError:
            print("Please enter a valid number for the model year")
    make = input("What is the car's make?: ")
    model = input("What is the car's model?: ")
    newcar = carclass.Car(year, make, model)

    # Call the acceleration method five times
    for count in range(5):
        newcar.accelerate()
        newcar.get_speed()
        print("The speed of the", year, make, model, "is increasing to: ", newcar.get_speed(), "mph.")

    # Call the deceleration method five times
    for count in range(5):
        newcar.brake()
        newcar.get_speed()
        print("The speed of the", year, make, model, "is decreasing to: ", newcar.get_speed(), "mph.")

# Call main
main()