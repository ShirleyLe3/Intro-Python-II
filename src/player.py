from item_container import ItemContainer

class Player(ItemContainer):
    def __init__(self, name, current_room):
        super().__init__(name)
        self.current_room = current_room
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
        super().give(item)
        item.on_take(self)

    def drop(self, item_name):
        item = self.__find_item__(item_name)
        if item is not None:
            if item.name == "lantern":
                print("I shouldn't drop this.")
            else:
                self.current_room.give(item)
                item.on_drop(self, self.current_room.name)
                self.__delete_item__(item)
        else:
            print(f"You checked your bag for [{item_name}] but found none.")

    def bag(self, item_name=None):
        if item_name is None:
            text = "In your bag you have...\n"
            if len(self.items) > 0:
                for item in self.items:
                    text += f"-[{item.name}]\n"
            else:
                text += "Nothing. Perhaps you should have brought something."
            print(text.rstrip())
        else:
            item = self.__find_item__(item_name)
            if item is not None:
                print(item.description)
            else:
                print(f"You checked your bag for [{item_name}] but found none.")

    def use(self, item_name):
        item = self.__find_item__(item_name)
        if item is not None:
            if item.name == "lantern":
                self.lantern_on = not self.lantern_on
                print(f"You turned {'on' if self.lantern_on else 'off' } the lantern.")
        else:
            print(f"You checked your bag for [{item_name}] but found none.")