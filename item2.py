import time
import sys
import pygame



class Item():
    def __init__(self, name, description = "", connection =""):
        self.name = name
        self.description = description
        self.connection = connection
    
    def which_room(self, room):
        room.items[self.name] = self

    # setters

    def set_name(self,name):
        self.name = name
        
    def set_description(self, description):
        self.description = description
        
    def set_connection(self, connection):
        self.connection = connection
    
    #getters
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def get_connection(self):
        return self.connection

class Interactive_Item(Item): # specific item that can't be picked up but can be 
    def __init__(self, name, description='', prize = None):
        super().__init__(name, description=description)
        del self.connection

        self.prize = prize
    
    def which_room(self, room):
        room.interactive_items[self.name] = self
    
    def reward(self, player):
        print("You activated the " + self.name + ".")
        #if there is an item to obtain, activate prize first
        if self.prize != None:
            print("You receive " + self.prize.description)
            player.inventory.append(self.prize)

        # if the item has a special action 
        if self.name == "mirror":
            def curse():
                sys.stdout.write("\r")
                sys.stdout.write("{:2d} seconds remaining.".format(remaining)) 
                sys.stdout.flush()
                time.sleep(1)
            print("10 seconds remaining")
            say_your_name = input("\n The curse is on you! Spell your name and feed the mirror! > ")
            if say_your_name != player.name[::-1]:
                for remaining in range(10, 5, -1):
                    curse()
                say_your_name = input("\n Oh mortal, reverse your thinking, reverse your writing! The curse is on you! Spell your name as the mirror would call it! > ")
            if say_your_name != player.name[::-1]:
                for remaining in range(5, 0, -1):
                    curse()
                sys.stdout.write("\n You are dead! Death embraces you as you choke on the ground like a miserable vermin, the last victim of the mansion...")
                sys.exit()
            else:
                pygame.mixer.quit()
                pygame.mixer.init()
                pygame.mixer.music.load(r"C:\Users\Lento\Downloads\150017__klankbeeld__horror-kids-02.wav")
                pygame.mixer.music.play(loops = -1)
                print("You broke the curse of the mansion.")
                print("Thousands of voices fill your head. You see faint shadows turning into sentient, ghastly kids.")
                time.sleep(5)
                print("The promise of a party, the promise of protection, the lies of weeping parents...and then, the dance of the Plague Death.")
                time.sleep(5)
                print("Dance with them, " + player.name + ". Dance with them as their souls roam free and yours stays in the mansion, oh prisoner of compassion.")
                print("""
           ______
        .-"      "-.
       /            \
      |              |
      |,  .-.  .-.  ,|
      | )(__/  \__)( |
      |/     /\     \|
      (_     ^^     _)
       \__|IIIIII|__/
        | \IIIIII/ |
        \          /
         `--------`""")
                time.sleep(10)
                sys.exit()
        
        #special object
        if self.name == "door":
            print("The door opens slowly as you mark it. There's the horrible echo of a thousand screams and then an ancient, forgotten silence.")
            print("There's a wall on the other side with tiny word written in a forgotten language.")
        

        # cancel item from list in room
        del player.current_room.interactive_items[self.name]
        
        

