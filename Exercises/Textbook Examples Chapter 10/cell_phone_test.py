__author__ = 'kadar'
import cellphone


def main():
    man = input('Enter the manufacturer: ')
    mod = input('Enter the model: ')
    price = float(input('Enter the retail price: '))

    phone = cellphone.CellPhone(man, mod, price)

    print('Here is the data that you entered: ')
    print('Manufacturer:', phone.get_manufact())
    print('Model Number:', phone.get_model())
    print('Retail Price: $', format(phone.get_retail_price(), ',.2f'), sep='')

main()