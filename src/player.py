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
            print("You've arrived at...")
        else:
            print("Cannot go that way.")

    def give(self, item):
        self.items.append(item)
        item.on_take()

    def drop(self, item_name):
        found = False
        for i, item in enumerate(self.items):
            if item.name == item_name:
                self.current_room.give(item)
                item.on_drop(self.current_room.name)
                del self.items[i]
                found = True
        if not found:
            print(f"You checked your bag for [{item_name}] but found none.")

    def bag(self, item_name = None):
        if item_name is None:
            text = "In your bag you have...\n"
            if len(self.items) > 0:
                for item in self.items:
                    text += f"-{item.name}\n"
            else:
                text += "Nothing. Perhaps you should have brought something."
            print(text)
        else:
            found = False
            for item in self.items:
                if item.name == item_name:
                    print(item.description)
                    found = True
            if not found:
                print(f"You checked your bag for [{item_name}] but found none.")