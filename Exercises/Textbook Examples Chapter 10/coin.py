__author__ = 'kadar'
import random


class Coin:
    def __init__(self):
        # self.sideup = 'Heads' -- this is not private, the attribute can be directly accessed
        self.__sideup = 'Heads'  # -- use of __ allows the attribute to be private and immutable

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def get_sideup(self):
        return self.__sideup