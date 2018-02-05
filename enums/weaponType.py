#!/usr/bin/python3

#----------------------------------------------------
# File name     : weaponTypes.py
# Despription   : Enum - Different Weapon types
# Author        : Romconstruct
# E-mail        : mail@romconstruct.org
# Website       : www.romconstruct.org
# Date          : 2018/02/05
#----------------------------------------------------

# Imports
from enum import Enum, auto

class WeaponType(Enum):
    AXE = auto()
    BLUNT = auto()
    BOW = auto()
    KNIFE = auto()
    HAMMER = auto()
    SWORD = auto()
    LONG_SWORD = auto()
