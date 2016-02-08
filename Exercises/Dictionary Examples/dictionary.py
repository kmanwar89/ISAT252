__author__ = 'kadar'
#these are the answers to the lab?

# search through dictionary using its key value
# phonebook = {'Chris':'555-1111', 'Kate':'555-2222','Joanne':'555-3333'}
# if 'Kate' in phonebook:
#     print(phonebook['Kate'])


# Add element to a dictionary
# phonebook = {'Chris':'555-1111','Katie':'555-2222','Joanne':'555-3333'}
# phonebook['Joe'] = '555-0123'
# phonebook['Chris'] = '555-4444'
# print(phonebook)

# delete element from a dictionary
# del dictionary[key]
# phonebook = {'Chris':'555-1111','Katie':'555-2222','Joanne':'555-3333'}
# del phonebook['Chris']
# print(phonebook)
# KeyError if a key is not present in the dictionary

# Getting the number of elements and mixing data types
# len() function

# phonebook = {'Chris':'555-1111','Katie':'555-2222','Joanne':'555-3333'}
# num_items = len(phonebook)
# print(num_items)

# use a for loop to iterate over a dictionary
# phonebook = {'Chris':'555-1111', 'Kate':'555-2222','Joanne':'555-3333'}
# for key in phonebook:
#     print(key)

phonebook = {'Chris':'555-1111', 'Kate':'555-2222','Joanne':'555-3333'}
for key in phonebook:
    print(key, phonebook[key])