from fight import letsFight
from account_handler import player
from world_creator import merchant
from constants import *
import library as lib



def displayHelpMenu():
    """Displays available commands."""
    print(18 * "*", "AVAILABLE COMMANDS", 18 * "*")
    print("- HELP: Shows this menu.")
    print("- ATTACK <ENEMY>: Attack someone! Or something!")
    print("- STATUS: Display information about yourself.")
    print("- TAKE <ITEM>: Add an item to your inventory.")
    print("- DROP <ITEM>: Discard of an item in your inventory.")
    print("- EQUIP <ITEM>: Equip an item, such as a helmet or weapon.")
    print("- UNEQUIP <ITEM>: Remove an equipped item.")
    print("- INVENTORY: List all the items your are carrying.")
    print("- UNLOCK: Use a key to unlock locks.")
    print("- OPEN: Open containers, such as chests.")
    print("- LOOT <TARGET>: Loot a slain enemy or a container.")
    print("- CONSUME <ITEM>: Drink a potion, or eat a biscuit.")
    print("- EXAMINE <ITEM>: Examine a thing or a room.")
    print("- LIGHT <ITEM>: Light a fire.")
    print("- EXTINGUISH <ITEM>: Put a fire out.")
    print("- GO <DIRECTION>: Go somewhere and do something.")
    print("- BUY <ITEM>: Buys an item from the shop.")
    print("- SELL <ITEM>: Sells an item to the shop.")
    print("- SAVE: Save your progress.")
    print("- QUIT: Leave the game, for some reason.")
    print(56 * "*")


def playerStatus():
    print(18 * "*", "THIS IS YOU", 18 * "*" )
    print(f"*\tPlayer Level: {player.getLevel()} \t XP: {player.getXP()}/{player.getLevel() * 200}")
    print(f"*\tPlayer Health: {player.getHP()} \t Armor: {player.getArmor()}")
    print(f"*\tStrength: {player.getStr()} \t\t Dexterity: {player.getDex()}")
    print(f"*\tCoins: {int(player.getCoin())}")
    if player.getWielded():
        print(f"*\tYou're wielding a {player.getWielded().getName()}\t\t") 
    if player.isEquipped("chestplate"):
        print(f"*\tYou're wearing a chestplate.")
    if player.isEquipped("helmet"):
        print(f"*\tYou're wearing a helmet.")   
    print(49 * "*")


def movePlayer(userMovement, currentRoom):
    """Checks if exits exists and moves the player if true."""
    if userMovement == "west":
        if currentRoom.getExitWest():
            return currentRoom.getExitWest()
        else: 
            print("You run into a wall.")
    elif userMovement == "east":
        if currentRoom.getExitEast():
            return currentRoom.getExitEast()
        else: 
            print("You run into a wall.")
    elif userMovement == "north":
        if currentRoom.getExitNorth():
            return currentRoom.getExitNorth()
        else: 
            print("You run into a wall.")
    elif userMovement == "south":
        if currentRoom.getExitSouth():
            return currentRoom.getExitSouth()
        else: 
            print("You run into a wall.")
    else:
        print("You can't go there.")
        

def attack(target, currentRoom):
    """Checks if target is in room and if true calls the letsFight() function."""
    if lib.canPlayerSee(currentRoom):
        if findObjectInRoom(currentRoom, target):
            item = findObjectInRoom(currentRoom, target)
            if item.getObjectType() == MONSTER and item.getIsAlive():
                letsFight(player, item)
                return True


def consume(item_to_consume, item_number=None):
    """Checks what potion you want to drink and if you have it, and alters stats accordingly."""
    if item_number:
        try:
            item_number = int(item_number)
            potion_list = []
            for item in player.getInventory():
                if item.getName() == POTION and item_to_consume.lower() == POTION:
                    potion_list.append(item)
            if item_number > len(potion_list) or item_number == 0:
                return False
            else:
                potion_list[item_number-1].setPotionEffect(player)
                player.getInventory().remove(potion_list[item_number-1])
                return True
        except ValueError:
            return False
    else:
        for item in player.getInventory():
            if item.getName() == POTION and item_to_consume.lower() == POTION:
                item.setPotionEffect(player)
                player.getInventory().remove(item)
                return True
                

def examineMonster(monster):
    """Prints the description and inventory of target monster."""
    print(monster.getDesc())
    if monster.getInventory():
        print("It's carrying:")
        lib.printInventory(monster)


def examine(toLookAt, currentRoom):
    """takes user input and examines thing depending on input"""
    for item in currentRoom.getObjects():
        defineExamine(toLookAt, item)
    for item in player.getInventory():
        if item.getName() == toLookAt.lower():
            print(item.getDesc())
    
    if not findObjectInPlayer(player, toLookAt) and not findObjectInRoom(currentRoom, toLookAt):
        print("That doesn't exist.") 
        

def defineExamine(toLookAt, item):
    """checks what type of item you want to examine in the room"""
    if item.getName().lower() == toLookAt.lower():
        if item.getObjectType() == MONSTER:
            examineMonster(item)
        elif item.getName().lower() == CHEST:
            print(item.getDesc())
            if item.getIsOpen():
                print("It contains:")
                lib.printInventory(item)
        elif item.getObjectType() == ITEM:
            print(item.getDesc())
        elif item.getName() == SHOP:
            print("He has these items for sale: ")
            for thing in item.getInventory():
                print(f"{thing.getName().title()} for {int(thing.getValue() * 1.2)} coins.")

        
def manageGear(command, item):
    """Checks if you have the equipment in inventory and if it is a piece of equipment. 
        If all is true changes equipment status accordingly."""
    for thing in player.getInventory():
        if thing.getName().lower() == item.lower() and thing.getItemType() == WEAPON:
            if command == EQUIP and not player.getWielded():
                player.setWielded(thing)
                return True
            elif command == EQUIP and player.getWielded():
                print("You're already wielding a weapon.")
                return False
            elif command == UNEQUIP and thing == player.getWielded():
                player.setUnwield(thing)
                return True
            elif command == UNEQUIP and not player.getWielded():
                print("You're not wielding anything.") 
                return False
        elif thing.getName().lower() == item.lower() and thing.getItemType() == ARMOR:
            if command == EQUIP and not player.isEquipped(item):
                player.setEquipArmor(item)
                player.setArmor(thing.getDamageMitigation())
                return True
            elif command == EQUIP and player.isEquipped(item):
                print("You're already wearing that.")
                return False
            elif command == UNEQUIP and player.isEquipped(item):
                player.setUnequipArmor(item)
                player.setArmor(-thing.getDamageMitigation())
                return True
            else:
                print("You're not wearing that item.")
                return False
    else:
        print("I can't do that.")   
        return False


def trade(arg, thing):
    """Trading items with the merchant!"""
    if arg.lower() == BUY:
        for item in merchant.getInventory():
            if item.getName().lower() == thing.lower() and player.getCoin() >= item.getValue():
                merchant.sell(item)
                merchant.setCoin(int(item.getValue() * 1.2))
                player.buy(item)
                player.setCoin(int(-item.getValue() * 1.2))
                player.setTotalWeight(item.getWeight())
                print(f"You purchased {item.getName()} for {int(item.getValue() * 1.2)} coins.")
                return True
            elif item.getName().lower() == thing.lower() and player.getCoin() < item.getValue():
                print("The Mechant says: 'You can't afford that item.'")
                return False
            else:
                print("The Merchant says: 'You can´t purchase that.'")
                return False
        else:
            print("The Merchant says: 'I dont have that.'")
    elif arg.lower() == SELL:
        for item in player.getInventory():
            if item.getName().lower() == thing.lower() and merchant.getCoin() >= item.getValue():
                if item.getItemType() == WEAPON and player.getWielded().getName() == thing.lower():
                    manageGear(UNEQUIP, thing)
                elif item.getItemType() == ARMOR and player.isEquipped(thing):
                    manageGear(UNEQUIP, thing)
                player.sell(item)
                player.setCoin(int(item.getValue() * 0.8))
                merchant.buy(item)
                merchant.setCoin(int(-item.getValue() * 0.8))
                player.setTotalWeight(-item.getWeight())
                print(f"You sold {item.getName()} for {int(item.getValue() * 0.8)} coins.")
                return True
            elif item.getName().lower() == thing.lower() and merchant.getCoin() < item.getValue():
                print("The Merchant says: 'I can't afford to buy that item from you, sorry!'")
                return False
        else:
            print("The Merchant says: 'You can't sell stuff you dont have!'")
            return False
    else:
        print("The Merchant says: 'Can't do that, sorry!'")


def takeItem(item_to_take, currentRoom):
    """If item in room inventory, remove from room and add to player inventory."""
    for item in currentRoom.getObjects():
        if item.getObjectType() == ITEM:
            if item.getName().lower() == item_to_take.lower() and lib.checkWeight(item):
                currentRoom.getObjects().remove(item)
                player.getInventory().append(item)
                player.setTotalWeight(item.getWeight())
                return True    


def dropItem(item_to_drop, currentRoom):
    """If item's in inventory, remove from inventory and add it to room inventory."""
    for item in player.getInventory():
        if item.getName().lower() == item_to_drop.lower():
            if item == player.getWielded():
                manageGear(UNEQUIP,item_to_drop)
            elif player.isEquipped(item_to_drop):
                manageGear(UNEQUIP, item_to_drop)
            elif item_to_drop == TORCH:
                item.setOnOff(False)
                player.setIlluminated(False)
            currentRoom.getObjects().append(item)
            player.getInventory().remove(item)
            player.setTotalWeight(-item.getWeight())
            return True


def lootCheck(currentRoom, target):
    """Checks if monsters are dead and adds their inventory to player inventory."""
    if findObjectInRoom(currentRoom, target):
        item = findObjectInRoom(currentRoom, target)
        if item.getObjectType() == MONSTER and item.getIsAlive() == False and item.getInventory():
            loot(item)
            return True
        elif item.getName() == CHEST and item.getIsOpen():
            loot(item)
            return True


def loot(item):
    """Loops through the objects inv and removes it from it and adds it to the player."""
    while item.getInventory():
        loot = item.getInventory().pop()
        player.getInventory().append(loot)


def lightExtinguish(command, item):
    """Checks if you have torch in inventory, lights it if true."""
    if findObjectInPlayer(player, item) and findObjectInPlayer(player, item).getName() == TORCH:
        torch = findObjectInPlayer(player, item)
        if command == LIGHT and not torch.getOn():
            torch.setOnOff(True)
            player.setIlluminated(True)
            return True
        elif command == LIGHT and torch.getOn():
            return False
        elif command == EXTINGUISH and torch.getOn():
            torch.setOnOff(False)
            player.setIlluminated(False)
            return True
        elif command == EXTINGUISH and not torch.getOn():
            return False


def openContainer(currentRoom, item):
    """Loops through the rooms object to see if theres a chest in there
       then checks whether the chest is locked or not and opens the chest accordingly"""
    for thing in currentRoom.getObjects():
        if thing.getName() == CHEST and item.lower() == CHEST and not thing.getIsOpen(): 
            if thing.getLock().getLocked():
                print(f"The {item.lower()} is locked.")
                return False
            elif not thing.getLock().getLocked():
                thing.setIsOpen(True)
                print(f"The {item.lower()} opens.")
                return True
        elif thing.getName() == CHEST and item.lower() == CHEST and thing.getIsOpen(): 
            print("It's already open.")
    else:
        print("You can't do that.")   
        return False


def unlock(currentRoom, item):
    if findObjectInRoom(currentRoom, item) and item == CHEST:
        if findObjectInPlayer(player, KEY):
            container = findObjectInRoom(currentRoom, item)
            return tryToUnlock(item, container)
        else:
            print("You don't have the matching key.")
    else:
        print("There is nothing to unlock.")


def findObjectInRoom(currentRoom, item):
    for thing in currentRoom.getObjects():
        if thing.getName().lower() == item.lower():
            return thing
    else:
        return False


def findObjectInPlayer(player, item):
    for thing in player.getInventory():
        if thing.getName().lower() == item.lower():
            return thing
    else:
        return False


def tryToUnlock(item, container):
    if container.getName() == item.lower():
        if container.getLock().getID() == findObjectInPlayer(player, KEY).getID():
            container.getLock().setLocked(False)
            print("You unlocked the chest.")
        else:
            return False
    else:
        print("You can't unlock that.")