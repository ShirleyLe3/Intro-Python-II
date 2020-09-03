# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
        self.lantern_on = False

    def __str__(self):
        return f"----------\n\nCurrent Location:\nRoom: {self.current_room.name}\nDescription: {self.current_room.get_desc(self.lantern_on)}\n=========="

    def move(self, direction):
        if self.current_room[direction] is not None:
            self.current_room = self.current_room[direction]
            print("You've arrived at...")
        else:
            print("Cannot go that way.")

    def give(self, item):
        self.items.append(item)
        item.on_take(self)

    def __find_item__(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
            else:
                return None

    def __delete_item__(self, item):
        for i, my_item in enumerate(self.items):
            if my_item.name == item.name:
                del self.items[i]
            else:
                break

    def drop(self, item_name):
        item = self.__find_item__(item_name)
        if item is not None:
            self.current_room.give(item)
            item.on_drop(self, self.current_room.name)
            self.__delete_item__(item)
        else:
            print(f"You checked your bag for [{item_name}] but found none.")

    def bag(self, item_name = None):
        if item_name is None:
            text = "In your bag you have...\n"
            if len(self.items) > 0:
                for item in self.items:
                    text += f"-[{item.name}]\n"
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