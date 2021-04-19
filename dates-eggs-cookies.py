age = input('How old are you? ')
print(f'On your next birthday, you will be {int(age) + 1}.')

egg_cartons = input('How many full egg cartons do you have? ')
loose_eggs = input('How many eggs are in your not-full egg cartons that you have? ')
eggs = (int(egg_cartons) * 12) + int(loose_eggs)
print(f'You have {eggs} eggs')

total_cookies = input('How many cookies do you have? ')
people = input('How many people are there? ')
cookies_per_person = int(total_cookies)/int(people)
print(f'Each person may have {cookies_per_person} cookies.')