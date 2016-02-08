__author__ = 'kadar'

# ROWS = 5
# COLS = 3
#
# def main():
#
#     values=[[0 for r in range(ROWS)] for c in range(COLS)]
#
#     for r in range(ROWS):
#         for c in range(COLS):
#             while r != 0 and c!=0:
#                 values[r][c] = int(input("Enter a value: "))
# main()
#
# ROWS = 5
# COLS = 3
#
# def main():
#     values = [[0, 0, 0],
#               [0, 0, 0],
#               [0, 0, 0],
#               [0, 0, 0],
#               [0, 0, 0]]
#
#     # fill the list with values from the user
#     for r in range(ROWS):
#         for c in range(COLS):
#             values[r][c]=int(input("Enter a value to fill the list: "))
#
#     # display the list
#     print(values)
#
# main()

def main():
    names = ['Peter', 'Paul', 'Mary', 'Joseph', 'Ruby', 'Pam']

    search = 'Ruby'

    if search in names:
        print("Hello Ruby")
    else:
        print("No RUby")
main()