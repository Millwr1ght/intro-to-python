print('Who are your friends? (type \'quit\' to exit)')
friends_list = []
friend = ''
while friend != 'quit':
    friend = input('Friend\'s name: ')
    if friend != 'quit':
        friends_list.append(friend)

print('\nYour friends:')
for name in friends_list:
    print(name)
