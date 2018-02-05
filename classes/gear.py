#!/usr/bin/python3

#----------------------------------------------------
# File name     : gear.py
# Despription   : Gear
# Author        : Romconstruct
# E-mail        : mail@romconstruct.org
# Website       : www.romconstruct.org
# Date          : 2018/02/05
#----------------------------------------------------

# Imports
from .armor import Armor
from .weapon import Weapon

class Gear:
    'All the gear'

    armor = []
    weapons = []
    items = {}

    def __init__(self, name=''):
        self.name = name
      
    # Armor
    def addArmor(self, _name, _weight, _arType):
        newArmor = Armor(_name, _weight, _arType)
        self.armor.append(newArmor)
        self.items[_name] = newArmor
    
    def removeArmor(self, _name):
        self.armor.remove(_name)
    
    def displayArmorCount(self):
        print ("Number of Armor ", len(self.armor))
    
    def getTotalArmorWeight(self):
        arWeight = 0

        if len(self.armor) > 0:
            for i in range (0, len(self.armor)):
                arWeight += self.armor[i].getWeight()

        return arWeight

    def displayTotalArmorWeight(self):
        print ("Total armor weight: ",  self.getTotalArmorWeight())

    def displayAllArmor(self):
        if len(self.armor) > 0:
            for i in range (0, len(self.armor)):
                print (self.armor[i])
        else:
            print ("No armor in gear list.")

    # Weapons
    def addWeapon(self, _name, _weight, _wpType):
        newWeapon = Weapon(_name, _weight, _wpType)
        self.weapons.append(newWeapon)
        self.items[_name] = newWeapon

    def removeWeapon(self, _name):
        self.weapons.remove(_name)
    
    def displayWeaponCount(self):
        print ("Number of Weapons ", len(self.weapons))
    
    def getTotalWeaponWeight(self):
        wpWeight = 0

        if len(self.weapons) > 0:
            for i in range (0, len(self.weapons)):
                wpWeight += self.weapons[i].getWeight()
                
        return wpWeight

    def displayTotalWeaponWeight(self):
        print ("Total weapon weight: ",  self.getTotalWeaponWeight())
    
    def displayAllWeapons(self):
        if len(self.weapons) > 0:
            for i in range (0, len(self.weapons)):
                print (self.weapons[i])
        else:
            print ("No weapons in gear list.")

    # Total gear
    def displayTotalGearCount(self):
        self.displayArmorCount()
        self.displayWeaponCount()

    def getTotalGearWeight(self):
        return self.getTotalArmorWeight() + self.getTotalWeaponWeight()

    def displayTotalGearWeight(self):
        self.displayTotalArmorWeight()
        self.displayTotalWeaponWeight()
    
    def displayItems(self):
        if len(self.items) > 0:
            for i in self.items:
                print ("- A", self.items[i])
        else:
            print ("No items in gear list.")