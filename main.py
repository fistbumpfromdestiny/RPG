import player_input as pi
import account_handler
from world_creator import caves, cave_1

currentRoom = cave_1

def main_menu(currentRoom):
    while True:
        currentRoom = pi.parsePlayerCommand(input("What do you want to do? > "), currentRoom)
 
if __name__ == '__main__':

    main_menu(currentRoom)

