""" 
WANDERER RPG by N Johnston

"""

game_playing = True

# initiate menu 'variables'
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
 ===========  Game Credits  =========== 

             Producer: Mill
             Designer: Mill
            Developer: MILL

         Sound Design: Mill
            Visual FX: Mill
            QA Tester: Mill

    Made possible by users like YOU,
               Thank you!
   
----------------------------------------
'''

menu_default = '''----------------------------------------
 ======  WANDERER --- Main Menu  ====== 

     1. START Game   2. HOW To Play
     3. ABOUT Info   4. LEAVE 
----------------------------------------
'''
menu_stuck = '''----------------------------------------
 ======  Wanderer --- Main Menu  ====== 

     1. START Game   2. HOW To Play
     3. ABOUT Info   no escape 
----------------------------------------
'''
menu_stuck_what = '''----------------------------------------
 ======  stuckwhat -- MAIN MENU  ====== 

      what game       play?
      about info      no escape 
----------------------------------------
'''
menu_what = '''----------------------------------------
 ======  whatever --- Main Menu  ====== 

     1. What GAME    2. How To Play
     3. About Info   4. LEAVE 
----------------------------------------
'''
menu_what_stuck = '''----------------------------------------
 ======  whatstuck -- Main Menu  ====== 

      what game       2. PLAY
      3. INFO         no escape 
----------------------------------------
'''
menu_what_game = '''----------------------------------------
 ======  whatever --- Main Menu  ====== 

     there is not any game to play
     & therefore you can not LEAVE 
----------------------------------------
'''

about_screen = ''
help_screen = ''
# opening title sequence
print(opening_sequence)


def menu(menu, *choices):
    # menu
    choice = ''
    while choice.upper() not in choices:
        print('...')
        choice = input(menu)
    print('----------------------------------------')
    return choice


while game_playing:
    choice_one = menu(menu_default, 1, 2, 3, 4, 'WANDERER',
                      'ABOUT', 'HOW', 'LEAVE', 'START')

    # about screen
    if choice_one.lower() == 'about' or choice_one == '3':
        choice_two = menu(' =========  About - WANDERER  ========= \nMillwright Gaming is a one-person game\ndevelopment team devoted to making high\nquality gaming experiences available at\naffordable prices. This version of\nWANDERER is the 2021 reboot of the 2015\nCLASSIC, originally available on Mill\'s\nTI-84 Graphing Calculator.', 'WANDERER', 'CLASSIC')
        if choice_two.lower() == 'WANDERER':
            # wanderer
            print()
        elif choice_two.lower() == 'CLASSIC':
            # classic
            print()

    # help screen
    elif choice_one.lower() == 'how' or choice_one == '2':
        choice_two = menu(' ===========  How To Play  ============\nAs you journey across the Deserts of\nIncarnadine, you will be presented with\nmany CHOICES, which will be displayed in\nFULLCAPS. You can then type the choice\nyou choose and suffer the consequences,\nwhich may lead to more choices.\n\nYour goal? exploration, treasure, and\nabove all, ADVENTURE.', 'ADVENTURE', 'CHOICES', 'FULLCAPS')
        if choice_two.lower() == 'adventure':
            # adventure is out there
            print()
        elif choice_two.lower() == 'choices':
            # many choices
            print()
        elif choice_two.lower() == 'fullcaps':
            # FULL CAPS TURNABOUT
            print()

    # exit game
    elif choice_one.lower() == 'leave' or choice_one == '4':
        choice_two = menu('\n\tTHANKS for PLAYING!\n', 'THANKS', 'PLAYING')
        if choice_two.lower() == 'thanks':
            # option 1
            print()
        elif choice_two.lower() == 'playing':
            # option 2
            print()

    # adventure begins...
    elif choice_one == '1' or choice_one.lower() == 'start':
        choice_two = menu(menu_what, 'GAME', 'LEAVE')
        if choice_two.lower() == 'game':
            # option 1
            print(menu_what_game)
            print('...')
            print('what game?')
            # END
        elif choice_two.lower() == 'leave':
            # option 2
            choice_three = menu(menu_what_stuck, 'PLAY', 'INFO')
            if choice_two.lower() == 'play':
                # option 1
                print()
            elif choice_two.lower() == 'info':
                # option 2
                print()

    # credits screen
    elif choice_one.upper() == 'WANDERER':
        choice_two = menu(credits_sequence, 'MILL', 'YOU')
        if choice_two.lower() == 'MILL':
            # me
            print()
        elif choice_two.lower() == 'YOU':
            # or you
            choice_three = menu(thanks_for_playing, 'QUIT', 'RESTART')
