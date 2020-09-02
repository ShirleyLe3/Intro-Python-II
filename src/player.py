# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    def __str__(self):
        return (f'-----\nRoom: {self.current_room.name}\nDescription: {self.current_room.description}\n-----')
    def move(self, direction):
        if self.current_room[direction] is not None:
            self.current_room = self.current_room[direction]
        else:
            print('Cannot go that way.')