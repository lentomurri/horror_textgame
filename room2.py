class Room():
    def __init__(self, chart, name, description, x = 0, y = 0):
        self.name = name 
        self.description = description

        self.x = x
        self.y = y
        self.coordinates = [self.x, self.y]

        self.map = chart
        #items in the room
        self.items = {}
        
        #if the player doesn't explore, the interactive items arent'available
        self.interactive_items = {}
        

        self.chart(chart)

        #stores rooms in map and checks if there's another with same name or position
    
    def chart(self, chart):
        storage = all(value != self.coordinates for value in chart.structure.values())
        if storage:
            chart.structure[self] = self.coordinates
        else:
            raise Exception("Coordinates already existing, please change room's x and y parameters.")
    
    #setters
    def set_name(self, name):
        self.name = name

    def set_coordinates(self, name):
        self.coordinates = coordinates

    #changes map 
    def set_map(self, chart):
        del self.map.structure[self.name]
        self.chart(chart)
        self.map = chart
