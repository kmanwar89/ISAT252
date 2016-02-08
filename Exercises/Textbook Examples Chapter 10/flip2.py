# Example of using a class in a separate module and importing it using the
# import function. This allows the main function to be as concise as
# possible while allowing great flexibility

import coin


def main():
    # the syntax here is variable_name = filename.ClassName()
    # In this case, my_coin is an instantiation of the Toss()
    # method in the coin module. coin is the name of the file
    # and .Toss() is the method saved within that file.
    # Same as using something like random.randint. random is
    # the name of the module, and randint is the function within
    # that module.

    my_coin = coin.Toss()

    print('This side is up:', my_coin.get_sideup())

    print('I am going to toss the coin ten times:')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

main()