#!/usr/bin/python3

#----------------------------------------------------
# File name     : weapon.py
# Despription   : Weapon
# Author        : Romconstruct
# E-mail        : mail@romconstruct.org
# Website       : www.romconstruct.org
# Date          : 2018/02/05
#----------------------------------------------------

from .item import Item
from enums.itemType import ItemType
from enums.weaponType import WeaponType

class Weapon(Item):
    'A Weapon'

    def __init__(self, _name, _weight, _wpType):
        Item.__init__(self, _name, _weight, ItemType.Weapon)
        self.wpType = _wpType
      
    def getWPType(self):
        return self.wpType
    
    def setWPType(self, _wpType):
        self.wpType = _wpType

    def getAttValue(self):
        return self.attValue
    
    def setAttValue(self, _val):
        self.attValue = _val
    
    def __str__(self):
        return "%s, it is a %s" % (self.name, self.wpType.name)