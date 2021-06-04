"""
WANDERER RPG
Author: N Johnston

"""

GAME_PLAYING = True
SAVE = False

# initiate menu 'screens'
opening_sequence = '''----------------------------------------
                        _      _
  \\  /\\  / /\\ |\\ | |`\\ |_ |^> |_ |^>
   \\/  \\/ /``\\| \\| |_/ |_ |`\\ |_ |`\\
                                 (C)2021
----------------------------------------

Welcome to WANDERER, the text-based RPG
adventure developed by Millwr1ght Gaming'''
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

----------------------------------------'''
menu_default = '''----------------------------------------
 ======  WANDERER --- Main Menu  ======

     1. START Game   2. HOW To Play
     3. ABOUT Info   4. LEAVE
----------------------------------------'''
menu_stuck = '''----------------------------------------
 ======  Wanderer --- Main Menu  ======

     1. START Game   2. HOW To Play
     3. ABOUT Info   no escape
----------------------------------------'''
menu_stuck_what = '''----------------------------------------
 ======  stuckwhat -- MAIN MENU  ======

      what game       play?
      about info      no escape
----------------------------------------'''
menu_what = '''----------------------------------------
 ======  whatever --- Main Menu  ======

     1. What GAME    2. How To Play
     3. About Info   4. LEAVE
----------------------------------------'''
menu_what_stuck = '''----------------------------------------
 ======  whatstuck -- Main Menu  ======

      what game       2. PLAY
      3. INFO         no escape
----------------------------------------'''
menu_what_game = '''----------------------------------------
 ======  whatever --- Main Menu  ======

     there is not any game to play
     & therefore you can not LEAVE
----------------------------------------'''
thanks_for_playing = '''----------------------------------------
 ======================================
 You did it. You made it to the ending.
 No more cyclical menus leading you to
 the same screen time and time again.

         Your madness can end.
   You can make a choice that matters:

        [SAVE & QUIT]     [QUIT]

----------------------------------------'''
true_thanks_for_playing = '''----------------------------------------
 ======================================
 You did it. You made it to the true
 ending. No more fighting, no  more
 pointless trivia questions, no more
 hunting for all those easter eggs we
 had hidden in the menu.

     The menu can finally be done.

  You can finally make a real choice!
    And that\'s what really matters:

        [RESTART]         [QUIT]

----------------------------------------'''
youve_been_here = '''----------------------------------------
 ======================================
 You did it. You made it to the ending.
 No more cyclical...

 wait a second...

 I know you. You've been here before.

 It says right here in my notes: "The
 test sub...ahem... the user has been
 thanked already once before."

 Why did you return? Did you think the
 game CODE would be merciful and let
 you out if you brute force your way
 through the end screens? That maybe
 -I- would be merciful?

----------------------------------------'''
about_screen = '''----------------------------------------
 =========  About - WANDERER  =========
 Millwright Gaming is a one-person game
 development team devoted to making
 high quality gaming experiences
 available at affordable prices. This
 version of WANDERER is the 2021 reboot
 of the 2015 CLASSIC, originally
 available on Mill\'s TI-84 Graphing
 Calculator.

----------------------------------------'''
help_screen = '''----------------------------------------
 ===========  How To Play  ============
 As you journey across the Deserts of
 Incarnadine, you will be presented
 with many CHOICES, which will be
 displayed  in FULLCAPS. You can then
 type the  choice you choose and suffer
 the  consequences, which may lead to
 more choices.

 Your goal? exploration, treasure, and
 above all, aDVENTURE.
----------------------------------------'''
no_choices = '''----------------------------------------
From here on out there are no more
choices. Technically, you chould choose
any word and it would do something.
Think about it. There are so many words!
Even now the menu processor is loading 
all the possible words into the choice-
wordinput matching algorit 

Traceback (most recent call last):
  File "wanderer-rpg.py", line 210, in menu()
    while (choice := input(menu)).upper() not in choices:
OverflowError: too many choices
'''
adventure_game = '''----------------------------------------
----------------------------------------'''
final_boss = '''----------------------------------------
 ======================================
 You find yourself in a large cavernous
 room. Between you and a door marked
 "True Exit" stands Millwr1ght, the one
 and only, the final boss of the full
 version of this game. He seems to be
 messing with the backend code of the
 game when he notices your vacant stare

    He presents you with two options:
     You can either ATTACK or BLOCK,
    Which one you choose is up to you

----------------------------------------'''
pre_capital = '''----------------------------------------


            are you sure

             [YES] [NO]


----------------------------------------'''
CAPITAL_PUNISHMENT = '''----------------------------------------
 ======================================
 
 BWA-HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA

 WELCOME TO WHAT IS NOW YOUR EXISTENCE!
 WELCOME TO FULLCAPS LAND! ALL FUTURE
 PROMPTS ARE FULLY FULLCAPS! YOU WILL
 HAVE NO IDEA AS TO WHICH KEYWORDS WILL
 ALLOW YOU TO PROCEED ON YOUR JOURNEY
 THROUGH THIS ENDLESS TORTURE MAZE OF A
 MAIN MENU! I MEAN WHO EVEN CAME UP
 WITH THIS!? THIS IS SUCH A BAD CONCEPT
 FOR A TEXT-BASED RPG, SO TEDIOUS HAVING TO DESIGN MENU AFTER MENU AFTER MENU

 WOAH. that's not supposed to happen ?

 ======================================
----------------------------------------'''


def menu(menu, *choices):
    """ the menu loop,
    while the user doesn't choose from the given list of choices, do nothing
    """
    while (choice := input(menu)).upper() not in choices:
        print('\n(Invalid selection)')
    print('----------------------------------------')
    return choice


def end_game():
    GAME_PLAYING = False


def main():
    """" the 'the main menu rpg game' game """

    # opening title sequence
    print(opening_sequence)

    while GAME_PLAYING:

        # start and restart
        choice_one = menu(menu_default, 1, 2, 3, 4, 'WANDERER',
                          'ABOUT', 'HOW', 'LEAVE', 'START')

        # about screen
        if choice_one.lower() == 'about' or choice_one == '3':
            choice_two = menu(about_screen, 'WANDERER', 'CLASSIC')
            # wanderer
            if choice_two.lower() == 'WANDERER':
                print('honestly, you should have gone with Classic. I just spent an hour porting the player movement part of a graphing calculator game I wrote in grade ten to python. I am dissapointed in you. But understanding. Here, have a second chance:\n\nrestarting WANDERER...')
                # go back to go, do not collect 200 dollars
            # classic
            elif choice_two.lower() == 'CLASSIC':
                GAME_PLAYING = old_game()

        # help screen
        elif choice_one.lower() == 'how' or choice_one == '2':
            choice_two = menu(help_screen, 'CHOICES', 'FULLCAPS')
            # many choices
            if choice_two.lower() == 'choices':
                print(no_choices)
                end_game()
            # FULL CAPS TURNABOUT
            elif choice_two.lower() == 'fullcaps':
                choice_three = menu(pre_capital, 'YES', 'NO')
                # yes
                if choice_three.lower() == 'yes':
                    choice_four = menu(CAPITAL_PUNISHMENT, 'WOAH', 'SKIP')
                    # opt1
                    if choice_four.lower() == 'woah':
                        print('----------------------------------------\n i know right? that\'s so cooool. i can go alllllllllllll the way past the edge of the screen now!\nwhat fun!\n\nWHOOPS. ACCIDENTALLY HIT THE CAPS LOCK KEY THERE. YOU SAW NOTHING. THERE IS ONLY FULLCAPS.\n\n ONLY FULLCAPS \n ONLY FULLCAPS \n ONLY FULLCAPS \n ONLY FULLCAPS \n ONLY FULLCAPS \n ONLY FULLCAPS \n ONLY FULLCAPS \n ONLY FULLCAPS \n ONLY FULLCAPS \n ONLY FULLCAPS \n ONLY FULLCAPS \n ONLY FULLCAPS \n ONLY FULLCAPS \n ONLY FULLCAPS \n ONLY FULLCAPS \n ONLY FULLCAPS \n ONLY FULLCAPS \n ONLY FULLCAPS \n ONLY FULLCAPS')
                        end_game()
                    # opt2
                    elif choice_four.lower() == 'skip':
                        print(
                            'Did you just? Skip? Could you always do that? Huh. \nImma go back there and fix that. Be right back. You go wait outside.')
                        end_game()
                # no
                else:
                    print(
                        'Why would you choose no? You could have had so much fun in All Caps Land. Here, try again.')

        # exit game
        elif choice_one.lower() == 'leave' or choice_one == '4':
            choice_two = menu('\n\tTHANKS for PLAYING!\n', 'THANKS')
            # thanks where thanks is due
            if choice_two.lower() == 'thanks' and not SAVE:
                print('You\'re Welcome!\n')
                choice_three = menu(thanks_for_playing, 'QUIT', 'SAVE')
                # 'end' the game but does it?
                if choice_three.lower() == 'save':
                    # the game restarts but...
                    SAVE = True

                # 'end' the game for realsies
                else:
                    print('huh...\nthat\'s strange...')
                    # psych

                    # you thought

            # you've been here before
            elif choice_two.lower() == 'thanks' and SAVE:
                choice_three = menu(youve_been_here, 'I', 'CODE', '')
                # python version 3
                if choice_three.lower() == 'code':
                    print('Made in Python 3.9.5 with VS Code')
                    end_game()

                # secret finishing move
                elif choice_three.lower() == 'i':
                    print(
                        'Gotta admit, "i" did not see that coming. I will allow that this time. You may pass.')
                    end_game()

                else:
                    print('You can\'t just put "nothing" as your answer!\nI\'m not even sure how you managed to submit "" as an answer!\nGo back to the beginning!\nI\'m restarting this madness just for that!')
                    # delete save file
                    SAVE = False

        # adventure begins...
        elif choice_one == '1' or choice_one.lower() == 'start':
            choice_two = menu(menu_what, 'GAME', 'LEAVE')
            # option 1
            if choice_two.lower() == 'game':
                print(menu_what_game)
                print('...\n\n\n...')
                print('what game?')
                # END
                end_game()

            # option 2
            elif choice_two.lower() == 'leave':
                print('I had this whole thing here where I wasn\'t gonna let you leave, and was all kinda boring. So here I am letting you out the backdoor.')
                print('Have a nice night!')
                # end_game()
                # ha nope
                print('\nsike no')

        # credits screen
        elif choice_one.upper() == 'WANDERER':
            choice_two = menu(credits_sequence, 'MILL', 'YOU')
            # choose me
            if choice_two.lower() == 'MILL':
                choice_three = menu(final_boss, 'ATTACK', 'BLOCK')
                # option 1
                if choice_three.lower() == 'attack':
                    print(
                        '\n"With what weapon? I don\'t think I\'ve seen you even pick one up yet!"')
                    # option 2
                elif choice_three.lower() == 'block':
                    print('"Uh... Okay then."')

                print('\nWhile you scramble for some way to attack the final boss, Mill uses his ultimate attack out of turn, killing your avatar.')
                end_game()

            # or you
            elif choice_two.lower() == 'YOU':
                choice_three = menu(thanks_for_playing, 'QUIT', 'RESTART')
                if choice_three.lower() == 'quit':
                    # option 1
                    end_game()

                # option 2
                # the game restarts

    print('Thanks for playing!')


# actual games
def old_game():
    """ the fancy game
    return : Boolean
    """
    play = True

    field = [[' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . '], [' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . '], [' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . '],
             [' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . '], [' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . '], [' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ']]

    x = 3
    y = 2

    print('CLASSIC WANDERER\n - WASD to move\n - ENTER to refresh the screen\n - QUIT to exit')
    while play:

        # place player
        field[y][x] = ' X '

        # draw field
        for row in field:
            for space in row:
                print(space, end='')
            print()

        # get input
        get_input = input('\n: ')
        if get_input.lower() == 'quit':
            play = False

        # advance
        field[y][x] = ' . '

        # up
        if get_input.lower() == 'w':
            # move the * up one row
            y -= 1

        # down
        elif get_input.lower() == 's':
            y += 1

        # left
        elif get_input.lower() == 'a':
            x -= 1

        # right
        elif get_input.lower() == 'd':
            x += 1

        # handle horizontal edges
        if x > 7:
            x = 0
        elif x < 0:
            x = 7

        # handle vertical edges
        if y > 5:
            y = 0
        elif y < 0:
            y = 5

    return False


if __name__ == '__main__':
    # old_game()
    main()
