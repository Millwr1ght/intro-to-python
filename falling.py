""" 
Team 5
Falling with Style
Drag and Velocity calculator
"""
from math import sqrt, exp, pi
print('Welcome to the Apeture Falling Testing Enrichment Centre. Please submit the following values:')

def velocity(m, g, p, A, C, t):
    c = 0.5 * p * C * A
    # formula for velocity at time (t)
    # v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))
    v = sqrt(m * g / c) * (1 - exp((-sqrt(m * g * c) / m) * t))

    print(f'\nThe calculated value of inner c: {c:.3f}')
    print(f'\nThe velocity at time {t}: {v:.3f}m/s')


def core_requirements():

    # get variables
    mass = float(input('Mass (in kg): '))
    gravity = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter, etc): '))
    time = float(input('Time (in seconds): '))
    density = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
    area = float(input('Cross-sectional area (in m^2): '))
    drag = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))

    velocity(mass, gravity, density, area, drag, time)


def challenge_one():
    """ determine the velocity for a few different objects that you know: a bowling ball, a loaf of bread, and a skydiver """
    # bowling ball: 5kg mass, 21.9cm diameter, 0.5 drag
    print('\nNow throw a bowling ball:')
    mass_ball = 5
    area_ball = pi * (.219/2 ** 2)
    drag_ball = 0.5

    gravity_ball = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter, etc): '))
    time_ball = float(input('Time (in seconds): '))
    density_ball = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))

    velocity(mass_ball, gravity_ball, density_ball, area_ball, drag_ball, time_ball)

    # bread_loaf
    print('\nNow for a loaf of bread:')
    mass_bread = .25
    area_bread = 1
    drag_bread = 1.1

    gravity_bread = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter, etc): '))
    time_bread = float(input('Time (in seconds): '))
    density_bread = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))

    velocity(mass_bread, gravity_bread, density_bread, area_bread, drag_bread, time_bread)
    challenge_three(mass_bread, gravity_bread, density_bread, drag_bread, area_bread)

    # skydiver
    print('\nLet us now think of a skydiver:')
    mass_diver = 75
    area_diver = .125
    drag_diver = 1.1

    gravity_diver = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter, etc): '))
    time_diver = float(input('Time (in seconds): '))
    density_diver = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))

    velocity(mass_diver, gravity_diver, density_diver, area_diver, drag_diver, time_diver)


def challenge_two():
    """ Compare the difference in velocities for two different gravity values (Earth and Jupiter), assuming everything else is the same """
    mass = float(input('Mass (in kg): '))
    time = float(input('Time (in seconds): '))
    density = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
    area = float(input('Cross-sectional area (in m^2): '))
    drag = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))

    print('On Earth:')
    velocity(mass, 9.8, density, area, drag, time)

    print('On Jupiter:')
    velocity(mass, 24, density, area, drag, time)


def challenge_three(m, g, p, C, A):
    """ one of the objects you picked, see if you can determine how long it takes to reach "terminal velocity" """
    # formula: v_terminal = sqrt(mg/c)
    c = 0.5 * p * A * C
    print(f'Terminal velocity: {sqrt(m * g / c):.3f}m/s')

if __name__ == '__main__':
    core_requirements()
    challenge_one()
    challenge_two()
