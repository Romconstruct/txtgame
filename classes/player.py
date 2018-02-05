#!/usr/bin/python3

#----------------------------------------------------
# File name     : player.py
# Despription   : Player Character
# Author        : Romconstruct
# E-mail        : mail@romconstruct.org
# Website       : www.romconstruct.org
# Date          : 2018/02/05
#----------------------------------------------------

# Imports
from .gear import Gear
from .character import Character

from const.config import Config
from const.message import Message
from enums.armorType import ArmorType
from enums.weaponType import WeaponType

class Player(Character):
    'The player'
    
    def __init__(self, _name='', _att=1, _def=1, _str=10):
        Character.__init__(self, _name, _att, _def)
        self.strength = _str
        self.gear = Gear()
        self.gear.addArmor('Robe', 2, ArmorType.CLOTH)
        self.gear.addWeapon('Mjölnir', 7, WeaponType.HAMMER)
    
    def showGear(self):
        self.gear.displayItems()
    
    def getStrength(self):
        return self.strength
    
    def setStrength(self, _str):
        self.strength = _str
    
    def getFreeCarry(self):
        return self.getTotalCarry() - self.gear.getTotalGearWeight() 

    def displayFreCarry(self):
        print(Message.FREE_CARRY, self.getFreeCarry())       

    def getTotalCarry(self):
        return self.strength * Config.MULTIPLIER_CARRY
    
    def displayTotalCarry(self):
        print(Message.TOTAL_CARRY, self.getTotalCarry())
    
    def __str__(self):
        return "%s is a monster" % (self.name)