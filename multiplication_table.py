num = int(input('Pick a number: '))
square_length = 1 + len(str(num**2))

for row in range(num):
    line = ''
    for column in range(num):
        line += f'{(row + 1)*(column + 1):{square_length}}'
    print(line)
