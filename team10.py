""" 
Week 10 : Lists in sync
"""

names = []
balances = []

# Ask the user for the name of the bank account and then for it's current balance.
name_of_account = ''
while name_of_account.lower() != 'quit':
    name_of_account = input('What is the name of the account? ')
    if name_of_account.lower() != 'quit':
        current_balance = float(input('What is the current balance? $'))

        names.append(name_of_account)
        balances.append(current_balance)

# iterate over both lists
editting = True
while editting:
    # print out all accounts
    for index in range(len(names)):
        print(f'{index}. {names[index]}: ${balances[index]:.2f}')

    # ask if they want to edit one
    user_input = input(
        'Do you want to change an account\'s information? (yes/no) ')
    if user_input.lower() == 'y' or user_input.lower() == 'yes':
        # choose an account
        account_to_edit = int(input('Which one? #'))
        new_name = input('Update name: ')
        new_balance = float(input('Update account balance: $'))
        balances[account_to_edit] = new_balance
        names[account_to_edit] = new_name

    elif user_input.lower() == 'n' or user_input.lower() == 'no':
        editting = False

# last, not in loop
print(f'Total balance: {sum(balances):.2f}')
print(f'Average balance: {sum(balances)/len(balances):.2f}')

max_value_index = balances.index(max(balances))
print(
    f'Highest balance: {names[max_value_index]} with ${balances[max_value_index]:.2f}')
