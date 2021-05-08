"""
Area of Shapes
CSE 110 - W03 Team Activity
Team 5

Write a program to compute the areas of three different shapes. Prompt for the necessary 
information, then compute and display the area, as follows:

* Square—The area is the length of a side squared.
* Rectangle—The area is the length multiplied by the width.
* Circle—The area is Pi (you can use 3.14) multiplied by the radius squared.

Make sure that your program can appropriately handle decimal values as well as whole numbers.

stretch challenges:
Instead of using 3.14 for your value of Pi, see if you can find and use the built-in value of Pi included
 in the python "math" module. Hint, you might try searching on the internet for something like, "python 
 how to get the value of pi."

Prompt the user for a single length value, then compute and display the areas of a square with that length
 of side, a circle with that radius, and then the volumes of a cube with that side and a sphere with that
 radius, all from the same value from the user.

For each of the three areas in the core requirements, change the prompt for the user to ask for the value
 in centimeters. Then, display the resulting area in both square centimeters and square meters. Keep in 
 mind that a centimeter is 1/100 of a meter, and a square centimeter is 1/10,000 of a square meter.
"""
from math import pi

# square area
side_length = float(input('What is the square\'s side length in cm? '))
square_area = side_length ** 2
print(square_area)
print('in meters:')
square_area_m = square_area * (1/100 ** 2)
print(square_area_m)

# rectangle area
width = float(input('What is the width of the rectangle in cm? '))
length = float(input('What is the length of the rectangle in cm? '))
rect_area = width*length
print(rect_area)
print('in meters:')
rect_area_m = rect_area * 1/10000
print(rect_area_m)

# circle area
circle_radius = float(input('What is the circle\'s radius length in cm? '))
circle_area = pi * circle_radius ** 2
print(circle_area)
print('in meters:')
circle_area_m =  pi * (circle_radius * 1/100) ** 2
print(circle_area_m)


""" # cube
cube_volume = side_length ** 3
print(cube_volume)

# sphere
sphere_volume = pi * 4/3 * side_length ** 3
print(sphere_volume) """
