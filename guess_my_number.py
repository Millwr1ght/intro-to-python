"""
Guess My Number (c)
W07 - Team activity

Goal 1: User chooses magic number, guesses it, program provides feedback
Goal 2: Program chooses the number, user guesses, program does feedback
Stretch 2: add a guesses counter
Stretch 3: add replay functionality
"""

from random import randint, seed
replay = True

# magic_number = int(input('What is your magic number? '))

while replay:
    # seed randint with a random number so that the number isn't 11 every. single. time.
    seed(randint(1, 100))

    print('Guess the magic number!')
    magic_number = randint(1, 100)
    
    guess = int(input('What is your guess? '))
    guesses = 1

    while magic_number != guess:
        if magic_number < guess:
            print('Lower')
        elif magic_number > guess:
            print('Higher')
        guess = int(input('What is your guess? '))
        guesses += 1

    print('You guessed it!')
    print(f'In {guesses} guesses!')

    play_again = input('\nPlay again? (y/n) ')
    if play_again.lower() == 'n' or play_again.lower() == 'no':
        replay = False

print('Thanks for playing!')