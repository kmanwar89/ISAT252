__author__ = 'kadar'
# Example of a class and a main function in the same file.  Fine for smaller
# programs but not good for future expansion/large & complex programs.
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


def main():
    my_coin = Coin()

    print('This side is up:', my_coin.get_sideup())

    print('I am going to flip the coin 10 times')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

main()