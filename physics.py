""" 

w04 team 5 team project : falling physics

"""
import math 


def v_formula(m, g, t, p, A, C):
    """ calc velocity and inner c """
    c = c_formula(p, A, C)
    v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))
    v_t = math.sqrt(m * g / c)
    return v_t, c, v


def c_formula(p, A, C):
    return 0.5 * p * A * C

print('Welcome to Team-5s falling calculator!')

mass = float(input('What is the mass? (in kg) '))
# gravity = float(input('What is the gravity? (in m/s^2, 9.8 for Earth, 24 for Jupiter) '))
time = float(input('How long has this been falling? (in seconds) '))
density = float(input('What is the density of the fluid? (in kg/m^3, 1.3 for air, 1000 for water) '))
area = float(input('What is the cross-sectional area of the object that is falling? (in m^2) '))
drag = float(input('What is the drag constant? (0.5 for sphere, 1.1 for cylinder) '))

v_terminal, inner_c, velocity = v_formula(mass, 9.8, time, density, area, drag)

print(f'\nThe inner c value is: {inner_c:.3f}')
print(f'The velocity at time {time} is: {velocity:.3f}')
print(f'Terminal velocity: {v_terminal:.3f}')
