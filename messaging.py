""" 
File: messaging.py
Author: N Johnston

This project was designed to help practice writing basic functions.
"""


def display_regular(message):
    """ Receives a string and prints it out, exactly as received. """
    print(message)


def display_uppercase(message):
    """ Receives a string, converts it to upper case, and then prints it out. """
    print(message.upper())


def display_lowercase(message):
    """ Receives a string, converts it to lower case, and then prints it out. """
    print(message.lower())


def main():
    """ main function """
    user_message = input('What is your message for the king? ')

    print()
    display_regular(user_message)
    display_uppercase(user_message)
    display_lowercase(user_message)


if __name__ == '__main__':
    main()
