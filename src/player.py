# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def __str__(self):
        return f"-----\nRoom: {self.current_room.name}\nDescription: {self.current_room.description}\n-----"

    def move(self, direction):
        if self.current_room[direction] is not None:
            self.current_room = self.current_room[direction]
        else:
            print("Cannot go that way.")

    def give(self, item):
        self.items.append(item)
        print(f"You took [{item.name}]")

    def drop(self, item_name):
        found = False
        for i, item in enumerate(self.items):
            if item.name == item_name:
                self.current_room.give(item)
                del self.items[i]
                found = True
        if not found:
            print(f"You checked your pockets for [{item_name}] but found none.")
