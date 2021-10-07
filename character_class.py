import random

class Character:
    """Initializes a template for character creation."""
    def __init__(self, name, item : list):
        self._name = name
        self._armor = 0
        self._level = 1
        self._hp = 40
        self._str = 1
        self._dex = 2
        self._isAlive = True
        self._damageModifier = 0
        self._xp = 0
        self._inventory = item
        self._wielded = False
        self._illuminated = False
        self._head = False
        self._chest = False
        self._coin = 0
        self._totalWeight = 0

    def getTotalWeight(self):
        """returns the total weight value on character"""
        return self._totalWeight
 
    def getIlluminated(self):
        """returns illuminated status"""
        return self._illuminated

    def getCoin(self):
        """returns the ammount of coins the player has"""
        return self._coin

    def getName(self):
        """returns character name"""
        return self._name

    def getHP(self):
        """returns character health"""
        return self._hp
    
    def getXP(self):
        """returns character XP"""
        return self._xp
    
    def getStr(self):
        """returns character strenght"""
        return self._str

    def getDex(self):
        """returns character dexterity"""
        return self._dex
    
    def getInventory(self):
        """returns character inventory"""
        return self._inventory

    def getIsAlive(self):
        """returns character dead/alive status"""
        return self._isAlive
    
    def getDamageModifier(self):
        """returns character damage modifiers"""
        return self._damageModifier 
    
    def getWielded(self):
        """returns character wielded status"""
        return self._wielded

    def getLevel(self):
        """returns character level"""
        return self._level

    def getArmor(self):
        """returns characters armor value"""
        return self._armor
    
    def isEquipped(self, arg):
        """checks if character is equipped with armor, if it´s a helmet return status for head or vice versa"""
        if arg == "helmet":
            return self._head
        elif arg == "chestplate":   
            return self._chest
    
    def setEquipArmor(self, arg):
        """sets status on helmet or chestplate as true if player equips helmet or chestplate"""
        if arg == "helmet":
            self._head = True
        elif arg == "chestplate":
            self._chest = True

    def setUnequipArmor(self, arg):
        """sets status on helmet or chestplate as false if player unequips helmet or chestplate"""
        if arg == "helmet":
            self._head = None
        elif arg == "chestplate":
            self._chest = None
    
    def setTotalWeight(self, arg):
        """sets a new total weight ammount on character depending on input argument"""
        self._totalWeight += arg
    
    def setIlluminated(self, arg):
        """sets characters illuminated status depending on input arugment"""
        self._illuminated = arg

    def setXP(self, XP):
        """method for changing character experience """
        self._xp += XP

    def setHP(self, newHP):
        """method for changing character health """
        self._hp += newHP
    
    def setStr(self, newStr):
        """method for changing character strenght"""
        self._str += newStr

    def setDex(self, newDex):
        """#method for changing character dexterity"""
        self._dex += newDex
    
    def setWielded(self, weapon):
        """checks if character is already wielded, if not sets wielded status to true and adds the weapons damage as a damage modifier"""
        self._wielded = weapon
        self._damageModifier += weapon.getDamage()
    
    def setUnwield(self, weapon):
        """sets character wielded status to false and removes weapons damage as damage modifier"""
        self._wielded = False
        self._damageModifier -= weapon.getDamage()

    def setArmor(self, arg):
        """changes characters armor value depending on argument"""
        self._armor += arg

    def setCoin(self, amount):
        self._coin += amount

    def takeDamage(self, dmg):
        """takes ammount of damage as argument, removes the armor value from that ammount. Also makes sure character cant take negative damage"""
        taken_dmg = dmg - self._armor
        if taken_dmg > 1: 
            self._hp = self._hp - taken_dmg
            return taken_dmg
        else:
            self._hp = self._hp - 1
            return 1

    def doDamage(self):
        """generates a random number between 1 and character strenght. If weapon is equipped it adds the weapons damage to character strenght"""
        return (random.randint(1, (self._str + self._damageModifier )))
           
    def levelUp(self):
        """method for character to level up and get better stats"""
        if self._xp >= self._level * 40:
            self._hp += 10
            self._str += 1
            self._dex += 1
            self._level += 1
            return True
        else:
            return False
        
    def buy(self, item):
        """method for buying item"""
        self._inventory.append(item)


    def sell(self, item):
        """method for selling item"""
        self._inventory.remove(item)