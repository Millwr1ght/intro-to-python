print('Welcome to Aperture Science\'s ID Badge Creator!')
first_name = input('Let\'s start with a few questions. What\'s your first given name? ')
last_name = input(f'Alright {first_name}, what\'s your last name? ')
email_address = input('And your email address? ')
phone_number = input('Phone number? ')
job_title = input('Alright, it\'s all coming together. What\'s your job title here at AS? ')
id_number = input('And finally, what is your ID number? ')

print('\nPrinting new ID Badge...\n')

print(f'''----------------------------------------
{last_name.upper()}, {first_name.capitalize()}
{job_title.title()}
ID: {id_number}

{email_address.lower()}
{phone_number}
----------------------------------------\n''')
