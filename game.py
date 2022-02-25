"""The game classes"""


class Room:
    """
    Class for room representation.
    """
    global rooms
    rooms = []
    def __init__(self, name: str, description='', room='', direction='', character='', item='') -> None:
        """
        create new room.
        """
        self.name = name
        self.description = description
        self.rooms = rooms
        self.room = room
        self.direction = direction
        self.character = character
        self.item = item


    def set_description(self, description):
        """
        Add description.
        """
        self.description = description        

    
    def link_room(self, room, direction: str):
        """
        Create new direction.
        """
        self.rooms.append((room, room.name, direction))
        self.room  = room
        self.direction = direction


    def set_character(self, character):
        """
        Set character.
        """
        self.character = character
    

    def get_character(self):
        """
        Get character.
        """
        return self.character


    def set_item(self, item):
        """
        Set item.
        """
        self.item = item


    def get_item(self):
        """
        Get item.
        """
        return self.item


    def get_details(self):
        """
        Print details.
        """
        print(self.name)
        print('--------------------')
        print(self.description)
        for i in self.rooms:
            print('The {} is {}'.format(i[1], i[2]))


    def move(self, command):
        """
        Move to new room.
        """
        for i in self.rooms:
            if command in i:
                return i[0]


class Enemy:
    """
    Class for enemy representation.
    """
    defeated = 0
    global characters
    characters = []
    def __init__(self, name: str, description: str, weakness = '', defeated = 0) -> None:
        self.name = name
        self.description = description
        self.weakness = weakness
        self.defeated = defeated
        characters.append(self)


    def set_conversation(self, conv: str):
        """
        Set conversation.
        """
        self.conversation = conv


    def set_weakness(self, weakness: str):
        """
        Set weakness.
        """
        self.weakness = weakness        
    

    def describe(self):
        """
        Print character`s description.
        """
        print('The {} is here!'.format(self.name))
        print(self.description)


    def talk(self):
        """
        Print character`s talk.
        """
        print('[{} says]: {}'.format(self.name, self.conversation))


    def fight(self, fight_with):
        """
        Fight with character.
        """
        if fight_with == self.weakness:
            return True
        return False


    def get_defeated(self):
        """
        Count defeated character.
        """
        for i in characters:
            i.defeated += 1
        return self.defeated


class Item:
    """
    Class for item representation.
    """
    def __init__(self, name, description='') -> None:
        """
        Create new item.
        """
        self.name = name
        self.description = description


    def set_description(self, description: str):
        """
        Set description.
        """
        self.description = description


    def get_item(self):
        """
        Get item.
        """
        return self.name

    
    def get_name(self):
        """
        Get name.
        """
        return self.name


    def describe(self):
        """
        Print description of the item.
        """
        print('The [{}] is here - {}'.format(self.name, self.description))
