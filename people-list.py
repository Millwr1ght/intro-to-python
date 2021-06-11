people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
youngest = 100
youngest_person = ''

for person in people:
    data = person.split()
    print(data)
    age = int(data[1])
    if age < youngest:
        youngest = age
        youngest_person = data[0]

print(f'Youngest: {youngest_person}, {youngest}')
