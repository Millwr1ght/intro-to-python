print('Welcome to Aperture Industries Cafeteria and Amusement Park!\nWe are pleased to introduce our newest ride this afternoon,\nthe Aerial Faith Plate Bouncy Castle!')
print('\nBecause of its extreme speed and lond falls, strict restrictions have been put in place for the safety of others.')
print('Please answer the following:')
can_ride = False
second_rider = False

user_age = int(input('How old are you? '))
user_height = int(input('What is your height in inches? '))
second_rider = input('Is there a second rider? (yes/no) ')
if second_rider.lower() == 'y' or second_rider.lower() == 'yes':
    second_rider = True
    second_rider_age = int(input('How old are they? '))
    second_rider_height = int(input('What is their height in inches? '))

if second_rider and (user_height >= 36 and second_rider_height >= 36):
    if user_age >= 18 or second_rider_age >= 18:
        can_ride = True
elif user_height >= 62 and user_age >= 18:
    can_ride = True

if can_ride:
    print('You may ride the Aerial Faith Plate Bouncy Castle. Please remain calm and keep hands and feet inside the ride at all times.')
else:
    print('You may not ride.')