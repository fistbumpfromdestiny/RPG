import sys
import commands as cmd
import library as lib
from account_handler import player, saveGame
from world_creator import caves, cave_5

_HELP = "help"
_TAKE_ITEM = "take"
_DROP_ITEM = "drop"
_EQUIP_ITEM = "equip"
_UNEQUIP_ITEM = "unequip"
_INVENTORY = "inventory"
_LOOT = "loot"
_STATUS = "status"
_CONSUME_ITEM = "consume"
_EXAMINE = "examine"
_LIGHT = "light"
_EXTINGUISH = "extinguish"
_GO = "go"
_BUY = "buy"
_SELL = "sell"
_ATTACK = "attack"
_QUIT = "quit"
_SAVE = "save"
_OPEN = "open"
_UNLOCK = "unlock"


_PLAYER_COMMANDS = [
    _HELP,
    _TAKE_ITEM,
    _DROP_ITEM,
    _EQUIP_ITEM,
    _UNEQUIP_ITEM,
    _INVENTORY,
    _LOOT,
    _STATUS,
    _CONSUME_ITEM, 
    _EXAMINE,
    _LIGHT, 
    _EXTINGUISH, 
    _GO,
    _BUY,
    _SELL,
    _ATTACK, 
    _QUIT, 
    _SAVE,
    _OPEN,
    _UNLOCK
]

ACTION = 0
TARGET = 1
NUMBER = 2

def parsePlayerCommand(playerCommand, currentRoom):
    try: 
        command = playerCommand.strip().split()
        if command == []:
            return currentRoom

        elif command[ACTION] not in _PLAYER_COMMANDS:
            print("Command doesn't exist.")

        elif command[ACTION] == _HELP:
            cmd.displayHelpMenu()

        elif command[ACTION] == _ATTACK:
            if not cmd.attack(command[TARGET], currentRoom):
                print("Invalid target.")

        elif command[ACTION] == _GO:                                    
            newCurrentRoom = cmd.movePlayer(command[TARGET], currentRoom)
            if newCurrentRoom != None:
                lib.printInterface(newCurrentRoom)
                return newCurrentRoom
            else:
                return currentRoom

        elif command[ACTION] == _EXAMINE:
            if lib.canPlayerSee(currentRoom):
                if command[TARGET] == "room":
                    lib.printInterface(currentRoom)
                else:
                    cmd.examine(command[TARGET], currentRoom)
            else:
                print("It´s too dark to see.")

        elif command[ACTION] == _STATUS:
            cmd.playerStatus() 

        elif command[ACTION] == _TAKE_ITEM:
            if lib.canPlayerSee(currentRoom):
                if cmd.takeItem(command[TARGET], currentRoom):
                    print(f"You take {command[TARGET]}.")
                else:
                    print("You can't take that.")  
            else:
                print("It's too dark to see.")

        elif command[ACTION] == _DROP_ITEM:
            if cmd.dropItem(command[TARGET], currentRoom):
                print(f"You dropped {command[TARGET]}.")       
            else:
                print("You don't have that item.")

        elif command[ACTION] == _INVENTORY:
            if player.getInventory():
                print("You're carrying:")
                lib.printInventory(player)

        elif command[ACTION] == _LOOT:

            if cmd.lootCheck(currentRoom, command[TARGET]):
                print(f"You loot it.")
            else:
                print("You can't loot that.")

        elif command[ACTION] == _LIGHT:
            if cmd.lightExtinguish(command[ACTION], command[TARGET]):
                print("You light the torch.")
            elif not cmd.lightExtinguish(command[ACTION], command[TARGET]):
                print("That can't be lit.")

        elif command[ACTION] == _EXTINGUISH:
            if cmd.lightExtinguish(command[ACTION], command[TARGET]):
                print("You put out the torch.")
            else:
                print("There is nothing to extinguish.")    

        elif command[ACTION] == _EQUIP_ITEM:
            if cmd.manageGear(command[ACTION], command[TARGET]):
                print(f"You equipped {command[TARGET]}.")

        elif command[ACTION] == _UNEQUIP_ITEM:
            if cmd.manageGear(command[ACTION], command[TARGET]):
                print(f"You unequipped {command[TARGET]}.")

        elif command[ACTION] == _CONSUME_ITEM:
            if len(command) < 3:
                if cmd.consume(command[TARGET]):
                    print("You feel refreshed.")
                else:
                    print("You can't consume that!")
            elif len(command) == 3:
                if cmd.consume(command[TARGET], command[NUMBER]):
                    print("You feel refreshed.")
                else:
                    print("You can't consume that!")
        
        elif command[ACTION] == _BUY:
            if currentRoom == cave_5:
                cmd.trade(command[ACTION], command[TARGET])
            else:
                print("You are nowhere near the shop!")
            
        elif command[ACTION] == _SELL:
            if currentRoom == cave_5:
                cmd.trade(command[ACTION], command[TARGET])
            else:
                print("You are nowhere near the shop!")

        elif command[ACTION] == _SAVE:
            saveGame(player, caves)
            print("Saved game.")

        elif command[ACTION] == _QUIT:
            saveGame(player, caves)
            print("An all encompassing voice bellows: \n")
            print(f"SEIZE, {player.getName().upper()}.\nYOU SHALL SOON BE AGAIN.")
            sys.exit()
        elif command[ACTION] == _OPEN:
            if lib.canPlayerSee(currentRoom):
                cmd.openContainer(currentRoom, command[TARGET])
            else:
                print("It's too dark to see.")
        
        elif command[ACTION] == _UNLOCK:
            if lib.canPlayerSee(currentRoom):
                cmd.unlock(currentRoom, command[TARGET]) 
            else:
                print("It's too dark to see.")               
        return currentRoom
                
    except IndexError:
        print(f"{command[0].title()} what?")
        return currentRoom