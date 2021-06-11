"""
File: check11.py
Author: Nathan Johnston

Open a file, read through it line by line, strip off leading and trailing whitespace and display each book to the screen
"""


def read(filepath):
    """counts all lines and words in a file, returns the values as a tuple"""

    with open(filepath) as open_file:
        for line in open_file:
            print(line.strip())


def main():
    """ the main function """
    file_to_read = 'check11\\books.txt'
    read(file_to_read)


if __name__ == "__main__":
    main()
