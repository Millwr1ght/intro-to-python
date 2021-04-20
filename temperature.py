#get input > temperature in degrees fahrenheit
fahrenheit = float(input('What is the temperature in Fahrenheit? '))

#process input > C = (F-32) * 5/9
celcius = (fahrenheit - 32) * 5 / 9

#output result
print(f'The temperature in Celcius is {celcius:.1f} degrees.')