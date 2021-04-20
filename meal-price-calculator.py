# Aperture Industries Cafeteria Meal Price Calculator
#             -----'processing' table-----
#
# input: price of child/adult meals, number of children/adults, sales tax rate
# processing: child meal price * number of children
#           + adult meal price * number of adults = subtotal
#             subtotal * tax rate = sales tax
#             subtotal + sales tax = total amount owed
#             amount owed - amount paid = change
# outputs: subtotal, sales tax, amount owed, change
#

print('Welcome to the Aperture Industries Cafeteria! We appreciate you and your choice to eat here.')
print('By using this meal calculator you give your tacit agreement to the Terms and Conditions, the Privacy Policy, and the Release for Use of Likeness. Other agreements may apply.')

# get input
child_meal = float(input('How much does a child\'s meal cost? '))
adult_meal = float(input('How much does an adult\'s meal cost? '))
number_of_children = int(input('How many children will be eating? '))
number_of_adults = int(input('How many adults will be eating? '))

# be snarky about number of guests
if number_of_children == 0:
    if number_of_adults >= 3:
        print('Oh, a party! What are you all celebrating?')
    elif number_of_adults == 2:
        print('Awww, what a cute couple!')
    elif number_of_adults == 1:
        print('You came to a restaurant, by yourself, on Valentine\'s Day? Oh hun.')

if number_of_adults <= 0 and number_of_children <= 0:
    print('Why are you like this. This is an error. We can\'t just be giving away guests like this.')

# finish inputs
sales_tax_rate = float(input('What is the local sales tax rate? '))
if sales_tax_rate > 0.15:
    print('That\'s quite the local sales tax. You must get great public benefits.')

# process inputs
subtotal = round((child_meal * number_of_children) +
                 (adult_meal * number_of_adults), 2)
sales_tax = subtotal * sales_tax_rate
total = subtotal + sales_tax

# output subtotals
print(f'Subtotal: ${subtotal:.2f}')
print(f'Tax: ${sales_tax:.2f}')
print(f'Total: ${total:.2f}\n')

# get payment and finish transaction
amount_owed = total
# while the user has a bill, ask them for money until they pay up 
while amount_owed > 0:
    amount_paid = float(input('What is the payment amount? '))
    amount_owed -= amount_paid
    if amount_owed > 0:
        print(f'You still owe us ${amount_owed:.2f}.')
change = abs(amount_owed)
print(f'Change: ${change:.2f}')