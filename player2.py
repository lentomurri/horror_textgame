
class Player():
    def __init__(self,map, x=0, y = 0, current_room = ""):
        self.name = input("Welcome, lonely wanderer...tell the Ancients your name... > ").strip()

        #where is the player
        self.x = x
        self.y = y
        self.position = [self.x, self.y]
        self.current_room = current_room
        self.map = map

        self.inventory = []
    
    def set_name(self, name):
        self.name = name.strip()
    
    def set_map(self, map):
        self.map = map
        self.position = [0,0]

    def get_name(self):
        return self.name

    # INVENTORY COMMAND

    def get_inventory(self):
        if self.inventory == []:
            print("No items")
        else:
            print("Your items: > ")
        for item in self.inventory:
            print(" > " + item.name + " - " + item.description)
    

    