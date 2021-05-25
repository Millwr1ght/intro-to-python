shopping_list = []

# Ask the user for a list of list of items in a shopping list, stop asking for items when the user types "quit."
print('Please enter the items of the shopping list (type: quit to finish):')
while (choice := input('Item: ')) != 'quit':
    shopping_list.append(choice)

# Loop through the items in the regular way
print('\nThe shopping list is:')
for item in shopping_list:
    print(item)

# Loop through the items using an index
print('\nThe shopping list with indexes is:')
for i in range(len(shopping_list)):
    print(f'{i}. - {shopping_list[i]}')

# Ask the user for an index and a new shopping list item.
replace = int(input('Which item would you like to change? '))
new_item = input('What is the new item? ')

# Replace the item at that index with the new item.
shopping_list[replace] = new_item

# Then, display the whole list again.
print('\nThe shopping list is:')
for item in shopping_list:
    print(item)
