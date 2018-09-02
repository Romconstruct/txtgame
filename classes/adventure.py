#!/usr/bin/python3

#----------------------------------------------------
# File name     : adventure.py
# Despription   : The main game
# Author        : Romconstruct
# E-mail        : mail@romconstruct.org
# Website       : www.romconstruct.org
# Date          : 2018/02/05
#----------------------------------------------------

# Imports
import io
import os
import random
import re

# Imports - Classes
from classes.player import Player
from classes.help import Help

# Imports - Constants
from const.commandMsg import CommandMSG
from const.helpMsg import HelpMSG
from const.errorMsg import ErrorMSG
from const.message import Message
from const.question import Question
from const.story import Story

# Imports - Tools
from tools.json_parser import jsonData

class Adventure(object):
    'The main adventure'
    def __init(self):
        self.keys = list(map(lambda x:re.compile(x[0], re.IGNORECASE),Story().gPats))
        self.values = list(map(lambda x:x[1],Story().gPats))

    #----------------------------------------------------------------------
    # translate: take a string, replace any words found in dict.keys()
    #  with the corresponding dict.values()
    #----------------------------------------------------------------------
    def translate(self, str, dict):
        words = str.lower().split()
        keys = dict.keys()
        for i in range(0,len(words)):
            if words[i] in keys:
                words[i] = dict[words[i]]
                return ' '.join(words)

    #----------------------------------------------------------------------
    #  respond: take a string, a set of regexps, and a corresponding
    #    set of response lists; find a match, and return a randomly
    #    chosen response from the corresponding list.
    #----------------------------------------------------------------------
    def respond(self, str):
         # find a match among keys
        for i in range(0, len(self.keys)):
            match = self.keys[i].match(str)
            if match:
                # found a match ... stuff with corresponding value
                # chosen randomly from among the available options
                resp = random.choice(self.values[i])
                # we've got a response... stuff in reflected text where indicated
                pos = resp.find('%')
                while pos > -1:
                    num = int(resp[pos+1:pos+2])
                    resp = resp[:pos] + \
                        self.translate(match.group(num),Story().gReflections) + \
                        resp[pos+2:]
                    pos = resp.find('%')
                # fix munged punctuation at the end
                if resp[-2:] == '?.': resp = resp[:-2] + '.'
                if resp[-2:] == '??': resp = resp[:-2] + '?'
                return resp
'''
    try:
        
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
'''