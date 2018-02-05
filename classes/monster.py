#!/usr/bin/python3

#----------------------------------------------------
# File name     : monster.py
# Despription   : Monster
# Author        : Romconstruct
# E-mail        : mail@romconstruct.org
# Website       : www.romconstruct.org
# Date          : 2018/02/05
#----------------------------------------------------

from .character import Character

class Monster(Character):
    'A Monster'

    def __init__(self, _name, _att, _def):
        Character.__init__(self, _name, _att, _def)
    
    def __str__(self):
        return "%s is a monster" % (self.name)