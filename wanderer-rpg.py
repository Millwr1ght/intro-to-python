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
            

    Made possible by users like you,
               Thank you!
   
----------------------------------------
'''

menu_1 = '''----------------------------------------
 ======  WANDERER --- MAIN MENU  ====== 

     1. START Game   2. HOW To Play
     3. ABOUT Info   4. LEAVE 
----------------------------------------
'''
menu_2 = '''----------------------------------------
 ======  WANDERER --- MAIN MENU  ====== 

     1. START Game   2. HOW To Play
     3. ABOUT Info   no escape 
----------------------------------------
'''

#opening title sequence
print(opening_sequence)

while gamemode_menu:
#menu
    menu_choice = input(menu_1)
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
        print('\n           Thanks for playing!\n\n\n\n\n\n')
        if has_awareness and not adventurous:
            print('...\n\n\n\n')
            print('...wait a second')
            print('You can\'t just QUIT! You haven\'t achieved the goals yet!')
            game_choice = input('There is still much ADVENTURE to be had! So much TREASURE!\n')
            if game_choice.lower() == 'adventure' or game_choice.lower() == 'treasure':
                print('I knew you would come around! I\'ll take you back to the MENU so you can start your ADVENTURE.')
                adventurous = True
            elif game_choice.lower() == 'quit':
                print('You think you\'re funny, eh? You think this is a joke!?')
                print('THERE IS NO ESCAPE! ONLY ADVENTURE!\n')
                print('in its fury, the game kills you.\nGAME OVER')
                game_running = False
            elif game_choice.lower() == 'sudo quit' or game_choice.lower() == 'sudo leave' or game_choice.lower() == 'sudo exit' or game_choice.lower() == 'sudo 4' or game_choice.lower() == 'sudo x':
                print('Ah. I see. As you were.')
                game_running = False
            else:
                print('Giving me that NONSENSE will do you no good on your ADVENTURE. Here, I will take you back to the MAIN MENU where you can start over.')
                has_nonsense = True
        elif adventurous:
            print('...\n\n\n\n')
            print('...wait a second')
            game_choice = input('You can\'t just QUIT! What happened to wanting to go on your ADVENTURE? You think I will just LET you leave? Do you think this is a GAME?\n')
            if game_choice.lower() == 'adventure' or game_choice.lower() == 'treasure':
                print('I knew you would come around! I\'ll take you back to the MENU so you can start your ADVENTURE.')
                adventurous = True
            elif game_choice.lower() == 'quit' or game_choice.lower() == 'let':
                print('You think you\'re funny, eh? You think this is a joke!?')
                print('THERE IS NO ESCAPE! ONLY ADVENTURE!\n')
                print('in its fury, the game kills you.\nGAME OVER')
                game_running = False
            elif game_choice.lower() == 'game':
                game_choice = input('I have some news for you buddy, it isn\'t a game. It is a text-based RPG adventure. See? NOT a game, an ADVENTURE!\n')
                if game_choice.lower() == 'adventure':
                    print('I knew you would come around! I\'ll take you back to the MENU so you can start your ADVENTURE.')
                elif game_choice.lower() == 'not' or game_choice.lower() == 'no':
                    print('That\'s right.\nNO ESCAPE\n')
                else:
                    print('Giving me that NONSENSE will do you no good on your ADVENTURE. Here, I will take you back to the MAIN MENU where you can start over.')
                    has_nonsense = True
            else:
                print('Giving me that NONSENSE will do you no good on your ADVENTURE. Here, I will take you back to the MAIN MENU where you can start over.')
                has_nonsense = True 
        else:
            game_running = False
#adventure begins
    elif menu_choice == '1' or menu_choice.lower() == 'start' or menu_choice.lower == 'adventure':
        gamemode_menu = False

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
            
