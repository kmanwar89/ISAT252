num = 0.0

num = float(input("Enter a number between 1 and 100: "))

while num < 1:
    print("Please enter a value between 1 and 100")
    num = float(input("Enter a number between 1 and 100: "))
while num > 100:
    print("Please enter a value between 1 and 100")
    num = float(input("Enter a number between 1 and 100: "))
print("Your value is: ", format(num, '.2f'))
