#!/usr/bin/python3

#----------------------------------------------------
# File name     : help.py
# Despription   : HELP
# Author        : Romconstruct
# E-mail        : mail@romconstruct.org
# Website       : www.romconstruct.org
# Date          : 2018/02/05
#----------------------------------------------------


# Imports
from const.commandMsg import CommandMSG
from const.helpMsg import HelpMSG

# Show Help or Commands list
class Help(object):
    'Game help'

    helpCMD = set('help' + 'h')
    commandsCMD = set('commands' +'c')

    @staticmethod
    def displayHelp():
        print(HelpMSG.DEFAULT_HELP)

    @staticmethod
    def displayCommands():
        print(CommandMSG.DEFAULT_COMMAND)
        print(CommandMSG.HELP_COMMAND)
        print(CommandMSG.LEFT_COMMAND)
        print(CommandMSG.RIGHT_COMMAND)
        print(CommandMSG.COMMANDS_LIST)

    @classmethod
    def showHelp(cls, cmd):
        if cmd in cls.helpCMD:
            return True
        else:
            return False
    
    @classmethod
    def showCommands(cls, cmd):
        if cmd in cls.commandsCMD:
            return True
        else:
            return False
    
    def __str__(self):
        return HelpMSG.DEFAULT_HELP + ' ' +CommandMSG.DEFAULT_COMMAND