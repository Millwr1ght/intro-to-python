child_meal = float(input('How much does a child\'s meal cost? '))
adult_meal = float(input('How much does an adult\'s meal cost? '))
number_of_children = int(input('How many children will be eating? '))
number_of_adults = int(input('How many adults will be eating? '))
sales_tax_rate = float(input('What is the local sales tax rate? '))

subtotal = round((child_meal * number_of_children) +
                 (adult_meal * number_of_adults), 2)
sales_tax = subtotal * sales_tax_rate
total = subtotal + sales_tax
print(f'Subtotal: ${subtotal:.2f}')
print(f'Tax: ${sales_tax:.2f}')
print(f'Total: ${total:.2f}')

amount_paid = float(input('What is the payment amount? '))
change = amount_paid - total
print(f'Change: ${change:.2f}')
