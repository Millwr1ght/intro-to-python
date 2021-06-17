""" 
File: team09.py
Authors: team this one

Lists
"""

# Ask the user for a series of numbers, and append each one to a list. Stop when they enter 0.
print('Enter a list of numbers! Type \'0\' when finished:')

list_of_numbers = []
answer = ''
while answer != 0:
    answer = int(input('Enter a number: '))
    if answer != 0:
        list_of_numbers.append(answer)

# Compute the sum, or total, of the numbers in the list.
print(f'Total: {sum(list_of_numbers)}')

# Compute the average of the numbers in the list.
print(f'Average: {sum(list_of_numbers)/len(list_of_numbers)}')

# Find the maximum, or largest, number in the list
print(f'Largest number: {max(list_of_numbers)}')

# Have the user enter both positive and negative numbers,
# then find the smallest positive number (the positive number that is closest to zero).

minimum = max(list_of_numbers)
for number in list_of_numbers:
    if number < minimum and number > 0:
        minimum = number

print(f'Smallest positive number: {minimum}')


# Sort the numbers in the list and display the new, sorted list. Hint: There are python libraries that can help you here, try searching the internet for them.
list_of_numbers.sort()
print('Sorted list: ', list_of_numbers)
