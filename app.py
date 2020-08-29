from item2 import Item, Interactive_Item
from player2 import  Player
from room2 import  Room
from game import Map, Game

#main map, stores rooms and coordinates
def main_game():
    main_map = Map()

# rooms
    kitchen = Room(main_map, "kitchen", "a small kitchen. There's the faint smell of rotten cabbage.", 0,0)
    ballroom = Room(main_map, "ballroom", "a beautiful ballroom. There are wooden puppets hanging, made for a kids' festival.", 0,1) 
    cellar = Room(main_map, "cellar", "a dump and humid cellar.", 1,1) 
    dining = Room(main_map, "a dining", "a warm dining room with the fireplace still burning even without woods.", 1,0) 

    player = Player(main_map, current_room=kitchen)

    # interactive items and their connection

    #MIRROR BRANCH
    mirror = Interactive_Item("mirror", "a decadent mirror. Your reflection stares at you - but is there a smug smirk on its face? There's a hole on the top. The inscription says 'Fill me with the blood gem.'")
    ruby = Item("ruby", "a magnificent ruby that shines wildly in the coldness of the house.", mirror)
    mosaic = Interactive_Item("mosaic", "the mosaic pictures an happy celebration in a medieval square. A piece is missing.", prize = ruby)
    stone = Item("stone", "a smooth, coloured stone. It looks like the piece of a puzzle.", mosaic)


    #BLOOD BRANCH
    door = Interactive_Item("door", """an unassuming door. You hear fainted voices through the keyhole. It says,
    'Mark me like Moses marked the Egyptian first born lambs.'""", prize = stone)
    blood = Item("blood", "dried blood from the withered corpse", door)
    meat = Interactive_Item("meat", """a chunk of flesh weirdly juicy and red. The rest of the corpse it comes from is grey and mummified.'""", prize = blood)
    knife = Item("knife", "a finely decorated knife used by royal butchers.", meat)

    #   SILVER KEY BRANCH
    statue = Interactive_Item("statue", """the statue of a weeping angel. There is an inscription.
                                    'Bring me back the sacred cup.'""", prize = knife)
    chalice = Item("chalice", "an ancient holy chalice used for rituals. The insides are stained in red.", statue)
    chest = Interactive_Item("chest",  "a silver chest ornated with unsettling images of burning kids. It says 'Property of Emerald Flower'", prize = chalice)
    key = Item("key", "a tiny, silver key with the letters 'EF'", chest)

    # ITEMS POSITION
    mirror.which_room(ballroom)
    mosaic.which_room(ballroom)

    door.which_room(cellar)
    meat.which_room(dining)

    statue.which_room(dining)
    chest.which_room(cellar)
    key.which_room(kitchen)

    game = Game(player, main_map)

main_game()

if __name__ == "__main__":
    main_game()