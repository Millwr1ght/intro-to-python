print('Welcome to Iowa Instruments Grade Calculation(c)\nWe are happy to interpret your grade for you!')
grade_percentage = float(input('What is your grade percentage? '))

#determine letter grade
if grade_percentage >= 90:
    letter_grade = 'A'
elif grade_percentage >= 80:
    letter_grade = 'B'
elif grade_percentage >= 70:
    letter_grade = 'C'
elif grade_percentage >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

#determine sign
last_digit = int(str(grade_percentage)[1])
letter_sign = ''
if grade_percentage >= 60 and grade_percentage < 93:
    if last_digit >= 7:
        letter_sign = '+'
    elif last_digit < 3:
        letter_sign = '-'

#return the results
print(f'Your grade: {letter_grade}{letter_sign}')
if grade_percentage >= 70:
    print('You passed!')
else:
    print('You fail! Better luck in your future endeavors')