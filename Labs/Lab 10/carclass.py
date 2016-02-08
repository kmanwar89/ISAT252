# Purpose: A class file used to create a Car object and define its' attributes
# Programmer: Kadar Anwar
# Language: Python 3.4
# carclass.py
# 4/20/2015 - ISAT 252

class Car:
    def __init__(self, year, make, model):
        self.__year = year
        self.__make = make
        self.__model = model
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed