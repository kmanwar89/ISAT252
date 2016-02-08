# Purpose: A class file used to create a pet object and define its' attributes
# Programmer: Kadar Anwar
# Language: Python 3.4
# petclass.py
# 4/20/2015 - ISAT 252

class Pet:
    def __init__(self, name, type, age):
        self.__name = name
        self.__type = type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, type):
        self.__type = type

    def set_age(self, age):
        self.__age = age

# Accessor methods to get the name, age and type of animal
    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_age(self):
        return self.__age