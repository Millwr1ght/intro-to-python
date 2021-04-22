#initiate the comparisons
correct_favorite_animal = 'Moose'
first_number = int(input('What is the first number? '))
second_number = int(input('What is the second number? '))

#compare numbers, is the first bigger?
if first_number > second_number:
    print('The first number is greater')
else:
    print('The first number is not greater')

#compare numbers, are they the same?
if first_number == second_number:
    print('The numbers are equal')
elif first_number != second_number:
    print('The numbers are not equal')

#compare numbers, is the second bigger?
if second_number > first_number:
    print('The second number is greater')
else:
    print('The second number is not greater')

#compare favorite animals, are the user's opinions objectively wrong?
incorrect_favorite_animal = input('\nWhat is your favorite animal? ')
if incorrect_favorite_animal.lower() == correct_favorite_animal.lower():
    print('Wow! That one is my favorite, too!')
else:
    print('That one is not my favorite.')