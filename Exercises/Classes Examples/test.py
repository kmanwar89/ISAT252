__author__ = 'kadar'
import Coin

def main():
    my_coin = Coin.Coin()

    print('This side is up:', my_coin.get_sideup())

    print('I am tossing the coin...')
    my_coin.toss()

    print('This side is up:', my_coin.get_sideup())

main()