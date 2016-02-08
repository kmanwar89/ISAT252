__author__ = 'kadar'
import bankaccount


def main():
    # Get starting balance
    start_bal = float(input('Enter your starting balance: '))

    # Create a BankAccount object
    # This passes the start_bal variable as an input to the
    # BankAccount object within the bankaccount.py module file
    # and assigns the memory location to the 'savings' variable
    savings = bankaccount.BankAccount(start_bal)

    # Deposit the user's paycheck
    print('Your account balance is $',
          format(savings.get_balance(), ',.2f'),
          sep='')

    # Get the amount to withdraw
    cash = float(input('How much would you like to withdraw?: '))
    print('I will withdraw that amount from your account')
    # Pass the cash argument to the withdraw method within the savings
    # class, which will call that method and have it perform some
    # operation on the 'cash' argument
    savings.withdraw(cash)

    # Display the balance
    print('Your account balance is: $',
          format(savings.get_balance(), ',.2f'),
          sep='')
# Call main
main()