#!/usr/bin/python3

#----------------------------------------------------
# File name     : armorType.py
# Despription   : Enum - Different Armor types
# Author        : Romconstruct
# E-mail        : mail@romconstruct.org
# Website       : www.romconstruct.org
# Date          : 2018/02/05
#----------------------------------------------------

# Imports
from enum import Enum, auto

class ArmorType(Enum):
    'Armor types'
    CLOTH = auto()
    LEATHER = auto()
    SCALE = auto()
    STUDDED_LEATHER = auto()
    PLATE = auto()