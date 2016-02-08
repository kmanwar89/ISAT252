__author__ = 'kadar'
# open the file to write
file = open('numbers_list.txt', 'w')

# use a loop to iterate 100 times
for i in range(1, 101):
    # convert the value to a string to be able to write and append a
    # newline
    output = str(i) + '\n'

    # write to the open file
    file.write(output)

# close the file
file.close()

