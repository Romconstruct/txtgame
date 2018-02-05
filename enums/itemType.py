#!/usr/bin/python3

#----------------------------------------------------
# File name     : itemType.py
# Despription   : Enum - Different types of items
# Author        : Romconstruct
# E-mail        : mail@romconstruct.org
# Website       : www.romconstruct.org
# Date          : 2018/02/05
#----------------------------------------------------

from enum import Enum, auto

class ItemType(Enum):
    'Types of items'
    Armor = auto()
    Weapon = auto()    