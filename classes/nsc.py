#!/usr/bin/python3

#----------------------------------------------------
# File name     : nsc.py
# Despription   : Non-Player-Character (NSC)
# Author        : Romconstruct
# E-mail        : mail@romconstruct.org
# Website       : www.romconstruct.org
# Date          : 2018/02/05
#----------------------------------------------------

# Imports
from enums.armorType import ArmorType
from enums.weaponType import WeaponType
from .gear import Gear
from .character import Character

class NSC(Character):
    'A NSC'

    def __init__(self, _name, _att, _def):
        Character.__init__(self, _name, _att, _def)
    
    def __str__(self):
        return "%s is a monster" % (self.name)