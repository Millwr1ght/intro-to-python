print('Welcome to Aperture Industries Cafeteria and Amusement Park!\nWe are pleased to introduce our newest ride this afternoon,\nthe Aerial Faith Plate Bouncy Castle!')
print('\nBecause of its extreme speed and lond falls, strict restrictions have been put in place for the safety of others.')
print('Please answer the following:')

# set default boolean values
can_ride = False
second_rider = False
user_has_passport = False
second_rider_has_passport = False

# get inputs
user_age = int(input('How old are you? '))
if user_age >= 12 and user_age <= 17:
    user_passport = input('Do you have a Golden Passport? (yes/no) ')
    if user_passport.lower() == 'y' or user_passport == 'yes':
        user_has_passport = True
user_height = int(input('What is your height in inches? '))

second_rider = input('Is there a second rider? (yes/no) ')
if second_rider.lower() == 'y' or second_rider.lower() == 'yes':
    second_rider = True
    second_rider_age = int(input('How old are they? '))
    if second_rider_age >= 12 and second_rider_age <= 17:
        second_rider_passport = input(
            'Do they have a Golden Passport? (yes/no) ')
        if second_rider_passport.lower() == 'y' or second_rider_passport == 'yes':
            second_rider_has_passport = True
    second_rider_height = int(input('What is their height in inches? '))

# determine eligibility
# if the user is taller than 36 inches
if user_height >= 36:
    # if there is a second rider and they are also taller than 36 inches
    if second_rider and second_rider_height >= 36:
        # if either rider is an adult
        if (user_age >= 18 or user_has_passport) or (second_rider_age >= 18 or second_rider_has_passport):
            can_ride = True
        # if both riders are 12 and are taller than 52 inches
        elif user_age >= 12 and user_height >= 52 and second_rider_age >= 12 and second_rider_height >= 52:
            can_ride = True
        # if one rider is at least 16 and the other is at least 14
        elif (user_age >= 16 and second_rider_age >= 14) or (user_age >= 14 and second_rider_age >= 16):
            can_ride = True
    # no second rider, if user is taller than 62 inches and is at least 18 or has a passport
    elif user_height >= 62 and (user_age >= 18 or user_has_passport):
        can_ride = True

if can_ride:
    print('You may ride the Aerial Faith Plate Bouncy Castle. Please remain calm and keep hands and feet inside the ride at all times.')
else:
    print('You may not ride.')
