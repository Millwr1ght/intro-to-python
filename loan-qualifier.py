print('Please rate the following questions on a scale from 1-10: ')
loan_size = int(input('How large is the loan? '))
credit_history = int(input('How good is your credit history? '))
income_size = int(input('How high is your income? '))
down_payment_size = int(input('How large is your down payment? '))

loan_the_user_money = False
if (loan_size >= 5 and ((credit_history >= 7 and income_size >= 7) or ((credit_history >=7 or income_size >= 7) and down_payment_size >=5))) or (credit_history >= 4 and((down_payment_size > 4 and income_size > 4) or (down_payment_size >= 7 or income_size >= 7))):
    loan_the_user_money = True

print('Decision:')
if loan_the_user_money:
    print('yes')
else:
    print('no')