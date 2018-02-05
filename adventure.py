#!/usr/bin/python3

#----------------------------------------------------
# File name     : adventure.py
# Despription   : A text Adventure/RPG with Python
# Author        : Romconstruct
# E-mail        : mail@romconstruct.org
# Website       : www.romconstruct.org
# Date          : 2018/02/05
#----------------------------------------------------

# Imports
import io
import re
import sys

from classes.player import Player
from classes.help import Help

from const.commandMsg import CommandMSG
from const.helpMsg import HelpMSG
from const.errorMsg import ErrorMSG
from const.message import Message
from const.question import Question
from const.story import Story

try:
    # Display welcome message
    print(Message.WELCOME_MSG)
    print(Message.HELP_INFO)
    
    while True: # Ask user for Character name
        name_str = input(Question.YOUR_NAME)

        if not re.match("^[a-zA-Z]*$", name_str):
            print (ErrorMSG.ERROR, ErrorMSG.DISALLOWED_CHARCTER)
        elif name_str == '':
            print (ErrorMSG.ERROR, ErrorMSG.NO_TEXT_ENTERED)
        elif Help.showHelp(name_str.lower()):
            Help.displayHelp()
        elif Help.showCommands(name_str.lower()):
            Help.displayCommands()
        elif len(name_str) > 10:
            print (ErrorMSG.ERROR, ErrorMSG.TEXT_ENTRY_LIMIT_REACHED)
        else:
            break
    
    player = Player(name_str)
    
    # Greet user
    print (Message.GREETING, player.getName())
  
    print(Message.STARTING_ITEM_INFO)
    player.showGear()
    player.displayTotalCarry()

    player.displayStats()
    
    # Begin adventure
    print (Story.WOOD_PATH)

    while True: # let player chose a path
        pathChoice = str(input(Question.CHOSE_PATH)).lower()

        if not re.match("^[a-zA-Z]*$", pathChoice):
            print (ErrorMSG.ERROR, ErrorMSG.DISALLOWED_CHARCTER)
        elif pathChoice.lower() in ['left', 'l']:
            print(Message.CHOSE_LEFT)
            break
        elif pathChoice.lower() in ['right', 'r']:
            print(Message.CHOSE_RIGHT)
            break
        elif Help.showHelp(pathChoice.lower()):
            Help.displayHelp()
        elif Help.showCommands(pathChoice.lower()):
            Help.displayCommands()
        else:
            print(Message.CANT_DECIDE)

except KeyboardInterrupt: # manual exit on Ctrl-C
    print (ErrorMSG.MANUAL_USER_EXIT)

except: # exception handling
    print (ErrorMSG.DEFAULT_ERROR)
    sys.exc_info()[0]
    raise