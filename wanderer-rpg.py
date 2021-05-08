#initiate variables
gamemode_menu = True
copyright_year = 2021
wanderer = 0
easter_eggs = 0
has_sword = False
has_book = False
has_awareness = False
has_magic = False
has_map = False
adventurous = False
stuck = False
opening_sequence = '''----------------------------------------
                        _      _     
  \\  /\\  / /\\ |\\ | |`\\ |_ |^> |_ |^> 
   \\/  \\/ /``\\| \\| |_/ |_ |`\\ |_ |`\\
                                 (C)2021
----------------------------------------

Welcome to WANDERER, the text-based RPG 
adventure developed by Millwr1ght Gaming
'''
credits_sequence = '''----------------------------------------
 ===========  GAME CREDITS  =========== 

             Producer: Mill
             Designer: Mill
            Developer: Mill

         Sound Design: Mill
            Visual FX: Mill
            QA Tester: Mill

    Made possible by users like you,
               Thank you!
   
----------------------------------------
'''

menu_default = '''----------------------------------------
 ======  WANDERER --- MAIN MENU  ====== 

     1. START Game   2. HOW To Play
     3. ABOUT Info   4. LEAVE 
----------------------------------------
'''
menu_stuck = '''----------------------------------------
 ======  WANDERER --- MAIN MENU  ====== 

     1. START Game   2. HOW To Play
     3. ABOUT Info   no escape 
----------------------------------------
'''
menu_what = '''----------------------------------------
 ======  WANDERER --- MAIN MENU  ====== 

     1. What GAME    2. HOW To Play
     3. ABOUT Info   4. LEAVE 
----------------------------------------
'''
menu_what_stuck = '''----------------------------------------
 ======  WANDERER --- MAIN MENU  ====== 

     1. what game    2. HOW To PLAY
     3. ABOUT Info   no escape 
----------------------------------------
'''
#opening title sequence
print(opening_sequence)
current_menu = menu_default

while gamemode_menu:
#menu
    menu_choice = input(current_menu)
    print('----------------------------------------')

#about screen
    if menu_choice.lower() == 'about' or menu_choice == '3':
        print(' =========  ABOUT - WANDERER  ========= \nMillwright Gaming is a one-person game\ndevelopment team devoted to making high\nquality gaming experiences available at\naffordable prices. This version of\nWANDERER is the 2021 reboot of the 2015\nclassic, originally available on Mill\'s\nTI-84 Graphing Calculator.')

#help screen
    elif menu_choice.lower() == 'help' or menu_choice.lower() == 'how' or menu_choice == '2':
        print(' ===========  HOW TO PLAY  ============\nAs you journey across the DESERTS of\nINCARNADINE, you will be presented with\nmany CHOICES, which will be displayed in\nFULLCAPS. You can then type the choice\nyou choose and suffer the consequences,\nwhich may lead to more choices.\n\nYour goal? EXPLORATION, TREASURE, and\nabove all, ADVENTURE.')
        has_awareness = True

#exit game
    elif menu_choice.lower() == 'leave' or menu_choice.lower() == 'x' or menu_choice.lower() == 'exit' or menu_choice == '4':
        print('\n\t\tThanks for playing!\n')
        game_running = False

#adventure begins
    elif menu_choice == '1' or menu_choice.lower() == 'start' or menu_choice.lower == 'adventure':
        gamemode_menu = False
        gamemode_menu = True
        """ ha. you thought. """
        if stuck:
            current_menu = menu_what_stuck
        else:
            current_menu = menu_what

#credits
    elif menu_choice.upper() == 'WANDERER':
        print(credits_sequence)
        
        wanderer += 1
        if wanderer == 3:
            #easter egg
            easter_eggs += 1

    else:
        #not a menu choice
        print('Please make a valid selection\n')



#gameplay begins
print('\n\nYou are jostled awake.')
has_not_moved = True
in_cart = True
while has_not_moved: 
    #user stays in this loop until they scootch CLOSER or JUMP off
    #this allows them to look around the CART
    game_choice = input('An old MAN sitting next to you in the back of this rickety wooden CART motions for you to come CLOSER.\n')
    if game_choice.lower() == 'man':
        print('On closer inspection, this old man seems and old. He is in no way frail, and looks like he plays nines. He wears long, midnight blue robes over his otherwise normal outfit.')
    elif game_choice.lower() == 'cart':
        print('The CART is rickety and wooden. It gets from place to place well enough, but the horses do need to be fed from time to time.')
        print('Looking around the cart, aside from the old man sitting in the back next to you, there is a CRATE, a SCROLL, and a FLASK')
    elif game_choice.lower() == 'crate':
        print('Ye cannot open ye CRATE. Yet.')
    elif game_choice.lower() == 'flask':
        print('Ye cannot get ye FLASK.')
    elif game_choice.lower() == 'scroll':
        print('You have found a map in the bottom of the CART!\n...\nIt\'s not a map of anywhere you recognize...')
        has_map = True
    elif game_choice.lower() == 'closer':
        print('You scootch CLOSER to the MAN.\n')
        has_not_moved = False
    elif game_choice.lower() == 'jump':
        print('In a burst of determined inspiration, you JUMP from the safety of the rickety wooden CART.')
        print('The burning desert surrounds you, embraces you.')
        print('The CART trundles away, leaving you alone with the burning SAND.')
        has_not_moved = False
        in_cart = False

if in_cart:
    #talk to old MAN
    print('The desert is no place for sleeping young one. It is dangerous to go alone, take this')            
            
