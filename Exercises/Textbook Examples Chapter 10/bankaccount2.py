__author__ = 'kadar'


class BankAccount:
    # the __init__ method accepts an argument of bal and assigns that value
    # as an attribute of the balance object
    def __init__(self, bal):
        self.__balance = bal

    # Deposit method - make a deposit in the account
    # My explanation - define a method called deposit, have it accept an
    # 'amount' as an argument. Create a private object called __balance.
    # Iterate & assign the value of that object by the 'amount' argument.
    def deposit(self, amount):
        self.__balance += amount

    # Withdraw method - withdraws money from the account
    # My explanation - define a method called withdraw that accepts an argument
    # of an amount. Use a conditional statement to ensure the balance is an
    # acceptable amount -- if not, it will display an error message.
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Error: Insufficient Funds')

    # get_balance method - get the current account balance
    # My explanation - return the 'balance' attribute that was
    # initially defined under the __init__(self) method by the argument
    # 'bal'
    def get_balance(self):
        return self.__balance

    # __str__ method - return a string indicating the objects' state
    def __str__(self):
        return 'The balance is $' + format(self.__balance, ',.2f')