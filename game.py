import re
import sys
import pygame as pg
from pygame import  mixer

class Map():
    def __init__(self):
        self.structure = {
            
        }

class Game():
    def __init__(self, player, map):
        self.player = player
        self.map = map
        pg.mixer.init()
        pg.mixer.music.load(r"C:\Users\Lento\Downloads\333220__robster881__horror-ambience.mp3")
        pg.mixer.music.play(loops = -1)
        self.start_game()
    
    def start_game(self):
        print("""
        ★ ° . *　　　°　.　°☆ 　. * ● ¸ 
. 　　　★ 　° :. ★　 * • ○ ° ★　 
.　 * 　.　 　　　　　. 　 
° 　. ● . ★ ° . *　　　°　.　°☆ 
　. * ● ¸ . 　　　★ 　° :●. 　 * 
• ○ ° ★　 .　 * 　.　 　　　　　.
 　 ° 　. ● . ★ ° . *　　　°　.　
°☆ 　. * ● ¸ . 　　　★ 　
° :. 　 * • ○ ° ★　 .　 * 　.　 
　★　　　　. 　 ° 　.  . 　    ★　 　　
° °☆ 　¸. ● . 　　★　★ 
° . *　　　°　.　°☆ 　. * ● ¸ . 
★ ° . *　　　°　.　°☆ 　. * ● ¸ 
. 　　　★ 　° :. 　 * • ○ ° ★　 
.　 * 　.　 　★     ° :.☆""")
        print("Welcome to the mansion, " + self.player.name + "...")
        self.help()
        self.command()
    
    def command(self):
        print("\n You find yourself in a " + self.player.current_room.description)
        command = input(" > : ").strip().lower()

        #associates command to right method

        if re.match(r"^explore", command):
            self.explore(self.player.current_room)
        if re.match(r"^help", command):
            self.help()
        if re.match(r"^inventory", command):
            self.player.get_inventory()
            self.command()
        if command in ["north", "south", "east", "west"]:
            self.move(command)
        if re.match(r"^quit", command):
            sys.exit()
        if re.match(r"^take", command):
            self.take(command)
        if re.match(r"^use", command):
            self.use(command)
        else:
            print("The mansion doesn't recognise this command.")
    
    # COMMANDS, ALPHABETICAL ORDER

    #returns a list of the items available to be picked and the items to interact with
    def explore(self, current_room):
        print("\n You can see and take these items around you: ")
        if self.player.current_room.items == {}:
            print("No items to pick up. \n")
        else:
            for item in self.player.current_room.items:
              print(" > " + item + " - " + self.player.current_room.items[item].description + "\n")
        if self.player.current_room.interactive_items != {}:
            print("You can use your items with these elements: ")
            for interactive_item in self.player.current_room.interactive_items:
                print(interactive_item + " - " + self.player.current_room.interactive_items[interactive_item].description + "\n")
        self.command()
        
    def help(self):
        print("""\n Your available commands are: 
> east/west/south/north: move player.
> explore: explore current room
> inventory: check your inventory
> take /item name/: takes item among listed ones
> use /item name/: uses item from inventory
> help: use it to refresh your memory about commands!
> quit: quit the mansion (and the game!)
Make sure you spell your commands and items right, bad writers are doomed in the grammar-nazi mansion! 
    """)
        self.command()

    def move(self, direction):
        # warning message if player moves out of map 
        warning = "You hit the wall. There's nothing in that direction."
        current_position = self.player.position

        #trial position before pushing to new one 
        # according to direction, add some and substract some
        if current_position[0] == 0 and direction == "north":
            current_position[0] = 1
        elif current_position[0] == 1 and direction == "south":
            current_position[0] = 0
        elif current_position[1] == 0 and direction == "east":
            current_position[1] = 1
        elif current_position[1] == 1 and direction == "west":
            current_position[1] = 0
        else:
            print(warning)
        self.player.position = current_position

        # finds current room and print description
        for room in self.map.structure:
            if self.player.position == self.map.structure[room]:
                self.player.current_room = room
        self.command()
    
    # ITEM COMMANDS
    # if item exists in room it gets added to the inventory
    def take(self, command):
        item = re.findall(r"^take\s([\w\W]+[?\s\w\W])", command)[0]
        for key in self.player.current_room.items:
            if item == key:
                self.player.inventory.append(self.player.current_room.items[item])
            else:
                "No such item available to take"
        del self.player.current_room.items[key]
        self.command()
    
    def use(self, command):
        item = re.findall(r"^use\s([\w\W]+[?\s\w\W])", command)[0].strip().lower()
        for obj in self.player.inventory:
            if obj.name == item:
                item = obj
                print("Use " + obj.name + " with what?")
                if self.player.current_room.interactive_items != {}:
                    for interactive_item in self.player.current_room.interactive_items:
                        print(interactive_item)
                else:
                    print("No interactive items in the room")
        # asks where you want to use the keys and lists interactive objects in the rooms
        interactive_item = input("")
        #checks if the interactive item is in the room  and if the item used is connected to the interactive one
        if interactive_item in self.player.current_room.interactive_items and item.connection.name == interactive_item:
            self.player.current_room.interactive_items[interactive_item].reward(self.player)
        else:
            print("Nothing happens. \n")
        self.command()