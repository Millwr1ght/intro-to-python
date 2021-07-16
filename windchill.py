"""
File: Windchill.py
Author: Nathan Johnston

Asks the user for a temperature and then shows the wind chill values for
    various wind speeds at that temperature.
To help users who are more familiar with Celsius, it allows temperatures 
    to be entered in either Celsius or Fahrenheit, and if needed, converts
    the Celsius temperature to Fahrenheit before using the formula.
"""


def calc_windchill(temperature, wind_speed):
    """
    The formula to calculate the wind chill factor is
    Wind Chill (ºF) --> f = 35.74 + 0.6215*t - 35.75*s^{0.16} + 0.4275*t*s^{0.16}

    where 
    f is the wind chill factor in Fahrenheit, 
    t is the air average temperature in Fahrenheit, and 
    s is the wind speed in miles per hour.

    :return: float
    """

    return 35.74 + (0.6215 * temperature) - (35.75 * (wind_speed ** 0.16)) + (0.4275 * temperature * (wind_speed ** 0.16))


def convert_c_to_f(temperature: float):
    """ 
    converts celcius to fahrenheit 
    :return: float
    """
    return (temperature * (9 / 5)) + 32


def prompt_temperature():
    """ 
    gets user input on temperature 
    :return: float
    """
    temp = float(input('What is the Temperature? '))
    letter = input('Fahrenheit or Celcius (F/C)? ')
    if letter.upper() == 'C':
        temp = convert_c_to_f(temp)
    return temp


def main():
    """ main function """
    # get the temperature
    temperature = prompt_temperature()

    # for each multiple of 5, calculate the windchill
    for speed in range(5, 65, 5):
        windchill = calc_windchill(temperature, speed)
        print(
            f'At {temperature:.1f}ºF, and with a wind speed of {speed} mph, the windchill is: {windchill:.2f}ºF')


if __name__ == '__main__':
    main()
