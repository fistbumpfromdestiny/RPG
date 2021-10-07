from merchant_class import Merchant
from room_class import *
from skeleton_class import Skeleton
from troll_class import Troll
from goblin_class import Goblin
from potion_class import Potion
from potionsize_class import PotionSize
from potiontype_class import PotionType
from torch_class import Torch
from statue_class import Statue
from lock_class import Lock
from chest_class import Chest
from key_class import Key
from axe_class import Axe
from sword_class import Sword
from armor_class import Armor
import account_handler as acc
import pickle


"""**********Creating All Items**********"""
potion_HP = Potion(PotionType.HP, PotionSize.BIG)
potion_STR = Potion(PotionType.STR, PotionSize.MEDIUM)
potion_DEX = Potion(PotionType.DEX, PotionSize.SMALL)
axe = Axe()
sword = Sword()
torch = Torch()
helmet = Armor('helmet', 'head', 2)
chestplate = Armor('chestplate', 'chest', 3)

"""**********Creating Objects**********"""

statue = Statue()
lock = Lock(1)
chest = Chest([statue], lock)
key = Key(1, "A small key.")

goblin = Goblin([torch, sword])
troll = Troll([key])
skeleton = Skeleton([helmet, chestplate, axe])

merchant = Merchant([potion_HP, potion_STR, potion_DEX])

"""**********World Creation**********"""

try:
    with open(f'{acc.player._name.lower()}/{acc.player._name.lower()}_caves.P', 'rb') as f:
        caves = pickle.load(f)
        cave_1, cave_2, cave_3, cave_4, cave_5 = caves

except:
    cave_1 = Room("A dark and funky cave room.", [goblin])
    cave_2 = Room("It's yet another dark and clammy cave room.", [chest])
    cave_3 = Room("The area is scattered with bones.", [troll])
    cave_4 = Room("A surprisingly tidy and clean area in the cave.", [skeleton])
    cave_5 = Room("The area seems magical, with a magical shop.", [merchant])
    caves = [cave_1, cave_2, cave_3, cave_4, cave_5]


cave_1.setExitWest(cave_2)
cave_1.setExitNorth(cave_3)
cave_1.setExitEast(cave_4)
cave_1.setExitSouth(cave_5)

cave_2.setExitEast(cave_1)
cave_2.setDark(True)

cave_3.setExitSouth(cave_1)

cave_4.setExitWest(cave_1)

cave_5.setExitNorth(cave_1)
