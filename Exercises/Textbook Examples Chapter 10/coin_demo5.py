__author__ = 'kadar'
import coin


def main():
    # create 3 objects from the Coin class
    coin1 = coin.Coin()
    coin2 = coin.Coin()
    coin3 = coin.Coin()

    # Display the side of each coin that is facing up
    print('I have three coins with these sides up')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()

    # Toss the coin
    print('I am tossing all three coins')
    print()
    coin1.toss()
    coin2.toss()
    coin3.toss()

    # Display the side of each coin that is facing up.
    print('Now here are the sides that are up:')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()

main()