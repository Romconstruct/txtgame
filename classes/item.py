#!/usr/bin/python3

#----------------------------------------------------
# File name     : item.py
# Despription   : Weapon
# Author        : Romconstruct
# E-mail        : mail@romconstruct.org
# Website       : www.romconstruct.org
# Date          : 2018/02/05
#----------------------------------------------------

# Imports
from enums.itemType import ItemType

class Item(object):
    'A item'

    def __init__(self, _name, _weight, _itemType):
        self.name = _name
        self.weight = _weight
        self.itemType = _itemType
    
    def getName(self):
        return self.name

    def setName(self, _name):
        self.name = _name
    
    def getType(self):
        return self.itemType
    
    def setType(self, _itemType):
        self.itemType = _itemType

    def getWeight(self):
        return self.weight
    
    def setWeight(self, _weight):
        self.weight = _weight
    
    def __str__(self):
        return "%s is a %s" % (self.name, self.itemType.name)
