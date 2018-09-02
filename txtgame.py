#!/usr/bin/python3

#----------------------------------------------------
# File name     : txtgame.py
# Despription   : A text Adventure/RPG with Python
# Author        : Romconstruct
# E-mail        : mail@romconstruct.org
# Website       : www.romconstruct.org
# Date          : 2018/02/05
#----------------------------------------------------

# Imports
import io
import sys

# Imports - Classes
from classes.adventure import Adventure

# Imports - Constants
from const.errorMsg import ErrorMSG
from const.message import Message

def game_cmd_interface():
    # Display welcome message
    print('='*72)
    print(Message.TITLE)
    print('='*72)
    print(Message.WELCOME_MSG)
    print('\n')
    print(Message.HELP_INFO)
    print(Message.COMMAND_INFO)
    print('='*72)

    s = ''
    game = Adventure()

    while s != 'quit':
        try:
            s = input('> ')
        except EOFError:
            s = 'quit'
        except KeyboardInterrupt: # manual exit on Ctrl-C
            print (ErrorMSG.MANUAL_USER_EXIT)
            s = 'quit'
        except: # exception handling
            print (ErrorMSG.DEFAULT_ERROR)
            sys.exc_info()[0]
            s = 'quit'
            raise
        print(s)
        while s[-1] in '!.':
            s = s[:-1]
            print(game.respond(s))

if __name__ == "__main__":
  game_cmd_interface()