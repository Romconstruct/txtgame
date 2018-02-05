#!/usr/bin/python3

#----------------------------------------------------
# File name     : character.py
# Despription   : Character
# Author        : Romconstruct
# E-mail        : mail@romconstruct.org
# Website       : www.romconstruct.org
# Date          : 2018/02/05
#----------------------------------------------------

# Show Help or Commands list
class Character(object):
    'A character in the game'

    def __init__(self, _name = '', _att = 1, _def = 1, _totalLife = 1):
        self.name = _name
        self.attack = _att
        self.defense = _def
        self.totalLife = _totalLife
        self.damage = 0

    def getName(self):
        return self.name
    
    def setName(self, _name):
        self.name = _name

    def getAttack(self):
        return self.attack
    
    def setAttack(self, _att):
        self.attack = _att
    
    def getDefense(self):
        return self.defense
    
    def setDefense(self, _def):
        self.defense = _def
    
    def getDamage(self):
        return self.damage

    def setDamage(self, _damage):
        self.damage = _damage
        
    def getCurrentLife(self):
        return self.totalLife - self.damage
    
    def getTotalLife(self):
        return self.totalLife
    
    def setTotalLife(self, _totalLife):
        self.totalLife = _totalLife
       
    def displayName(self):
        print ("Charcter name: ", self.name)
    
    def displayStats(self):
        if self.getCurrentLife() < self.totalLife:
            print ("Life:", self.getCurrentLife(), "|", self.totalLife)
        else:
            print ("Life:", self.totalLife)
        if self.damage > 0:
            print ("Damage: ", self.damage)
        print ("Attack: ", self.attack)
        print ("Defense: ", self.defense)
    
    def __str__(self):
        return "Player %s" % (self.name)
    