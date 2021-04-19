# import math functions and constants
import math

# determine which challenge to do #for debugging
print('Which activity do you want to do?')
print('1. Calculate the areas of shapes of varying sizes')
print('2. Calculare the areas of shapes of one length')
print('3. Calculate the areas of these shapes but in metric units')
choice = input('Choose one: ')

if choice == '2':
    # calculate volume of a cube == length ** 3
    length = float(input(
        'What is the length of the square and cube sides as well as the circle and sphere\'s radius? (input one(1) number) '))
    square_area = length ** 2
    circle_area = round(math.pi * length ** 2, 2)
    cube_volume = length ** 3
    sphere_volume = round(math.pi * 4/3 * (length ** 3), 2)
    print(f'The area of the square is: {square_area} units^2')
    print(f'The volume of the cube is: {cube_volume} units^3')
    print(f'The area of the circle is: {circle_area} units^2')
    print(f'The volume of the sphere is: {sphere_volume} units^3')

elif choice == '3':
    # calculate area of a square == length * length
    square_length = float(
        input('What is the length of a side of the square in centimetres? '))
    square_area = square_length ** 2
    # convert to meters
    square_area_m = (square_length/100) ** 2
    print(f'The area of the square is: {square_area} cm^2')
    print(f'The area of the square in meters is: {square_area_m} m^2')

    # calculate area of a rectangle == length * width
    rect_length = float(
        input('What is the length of rectangle in centimetres? '))
    rect_width = float(
        input('What is the width of the rectangle in centimetres? '))
    rect_area = rect_length * rect_width
    # convert to meters
    rect_area_m = (rect_length/100) * (rect_width/100)
    print(f'The area of the rectangle is: {rect_area} cm^2')
    print(f'The area of the rectangle in meters is: {rect_area_m} m^2')

    # calculate area of a circle == PI * radius * radius
    circle_radius = float(
        input('What is the radius of the circle in centimetres? '))
    circle_area = round(math.pi * circle_radius ** 2, 2)
    # convert to meters
    circle_area_m = round(math.pi * (circle_radius/100) ** 2, 2)
    print(f'The area of the circle is: {circle_area} cm^2')
    print(f'The area of the circle in meters is: {circle_area_m} m^2')

else:
    # calculate area of a square == length * length
    square_length = float(
        input('What is the length of a side of the square? '))
    square_area = square_length ** 2
    print(f'The area of the square is: {square_area} units^2')

    # calculate area of a rectangle == length * width
    rect_length = float(input('What is the length of rectangle? '))
    rect_width = float(input('What is the width of the rectangle? '))
    rect_area = rect_length * rect_width
    print(f'The area of the rectangle is: {rect_area} units^2')

    # calculate area of a circle == PI * radius * radius
    circle_radius = float(input('What is the radius of the circle? '))
    circle_area = round(math.pi * circle_radius ** 2, 2)
    print(f'The area of the circle is: {circle_area} units^2')
