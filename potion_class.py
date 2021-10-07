from potionsize_class import PotionSize
from potiontype_class import PotionType
from items_class import Item
 
class Potion(Item):
    
    def __init__(self, potion: PotionType, potency: PotionSize):
        super().__init__()
        self._potion = potion
        self._potency = potency
        self._weight = 1
        self._name = "potion"
        self._value = 10
        
    def getWeight(self):
        return self._weight

    def getPotionType(self):
        return self._potion
  
    def getPotionPotency(self):
        return self._potency

    def getPotionEffect(self):
        return self._potion
    
    def getObjectType(self):
        return self._objectType

    def getName(self):
        return self._name

    def getDesc(self):
        """Returns a description of the potion, ranging from a small to big 
        str/dex/hp/xp/invis potion."""
        if self._potency == PotionSize.SMALL:
            flask_size = "small"
        elif self._potency == PotionSize.MEDIUM:
            flask_size = "medium"
        elif self._potency == PotionSize.BIG:
            flask_size = "big"

        if self._potion == PotionType.HP:
            potion_name = "health"
        elif self._potion == PotionType.STR:
            potion_name = "strength"
        elif self._potion == PotionType.DEX:
            potion_name = "dexterity"
        elif self._potion == PotionType.XP:
            potion_name = "experience"
        elif self._potion == PotionType.INVIS:
            potion_name = "invisibility"

        return f"A {flask_size} potion of {potion_name}."    
    
    def setPotionEffect(self, player):
        
        if self._potion == PotionType.HP:
            player.setHP(self._potency * 15)

        elif self._potion == PotionType.STR:
            player.setStr(self._potency)
        
        elif self._potion == PotionType.DEX:
            player.setDex(self._potency)

        elif self._potion == PotionType.XP:
            player.setXP(self._potency * 50) 