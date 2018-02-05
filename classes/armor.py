#!/usr/bin/python3

#----------------------------------------------------
# File name     : armor.py
# Despription   : Armor
# Author        : Romconstruct
# E-mail        : mail@romconstruct.org
# Website       : www.romconstruct.org
# Date          : 2018/02/05
#----------------------------------------------------

from .item import Item
from enums.itemType import ItemType
from enums.armorType import ArmorType

class Armor(Item):
    'An armor'

    def __init__(self, _name, _weight, _arType):
        Item.__init__(self, _name, _weight, ItemType.Armor)
        self.arType = _arType
    
    def getARType(self):
        return self.arType
    
    def setARType(self, _arType):
        self.arType = _arType

    def getDefValue(self):
        return self.defValue
    
    def setDefValue(self, _val):
        self.defValue = _val
    
    def __str__(self):
        return "%s, it is made out of %s" % (self.name, self.arType.name)