def magic(num):
    return num + (num%3)**2

def main():
    num = float(input("Please enter a number"))
    print (magic(num))


main()
