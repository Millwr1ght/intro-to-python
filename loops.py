def pick_a_positive():
    """
    prompt the user for a positive number
    when they dont, ask again and again until they do
    """
    number = input('Pick a positive number: ')
    while number[0] == '-':
        print(f'Sorry, but {number} is not positve. Try again.')
        number = input('Pick a positive number: ')
    print(f'The number is {number}.')


def may_i_have_candy():
    """
    Ask for candy until the user says 'yes'
    """
    answer = 'no'
    while answer.lower() != 'yes':
        if answer.lower() != 'no':
            print('...')
        answer = input('May I have a piece of candy? ')
    print('Thank you.')


def main():
    """
    Week 07, Checkpoint A
    """
    # pick_a_positive()
    may_i_have_candy()


if __name__ == "__main__":
    main()
