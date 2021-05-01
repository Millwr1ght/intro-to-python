def grade_calculate(grade_percentage):
    """
    compare grade to tables, build and return grade string
    grade string should have a letter and a sign
    """
    if len(grade_percentage) >= 2:
        last_digit = int(grade_percentage[1])
    else:
        last_digit = int(grade_percentage[0])
    grade_percentage = float(grade_percentage)

    # build grade_string
    letter = grade_letter(grade_percentage)
    sign = grade_sign(grade_percentage, last_digit)
    grade_string = f'{letter}{sign}'

    # did they pass?
    passfail = did_you_pass(grade_percentage)
    return grade_string, passfail


def grade_letter(grade):
    """
    determine letter grade
    letter ranges: A >= 90, B >= 80, C >= 70, D >= 60, F < 60
    """
    if grade >= 90:
        letter_grade = 'A'
    elif grade >= 80:
        letter_grade = 'B'
    elif grade >= 70:
        letter_grade = 'C'
    elif grade >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    return letter_grade


def grade_sign(grade, digit):
    """
    determine sign
    sign: 0-3 == '-', 4-6 == '', 7-9 == '+'
    """
    letter_sign = ''
    if grade >= 60 and grade < 93:
        if digit >= 7:
            letter_sign = '+'
        elif digit < 3:
            letter_sign = '-'
    return letter_sign


def did_you_pass(grade):
    if grade >= 70:
        return True
    else:
        return False


def main():
    """
    05 Teach: Team Activity
    Grade Calculator
    https://byui-cse.github.io/cse110-course/lesson05/teach.html

    Write a program that determines the letter grade for a course according to the following scale:
    A >= 90, B >= 80, C >= 70, D >= 60, F < 60
    """
    print('Welcome to Iowa Instruments Grade Calculation(c)\nWe are happy to interpret your grade for you!')
    grade_percent = input('What is your grade percentage? ')
    grade, passed = grade_calculate(grade_percent)
    # return the results
    print(f'Your grade: {grade}')
    if passed:
        print('You passed!')
    else:
        print('You fail! Better luck in your future endeavors')


if __name__ == '__main__':
    main()
