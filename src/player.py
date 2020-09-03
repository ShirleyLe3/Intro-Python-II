from item_container import ItemContainer

class Player(ItemContainer):
    def __init__(self, name, current_room, world):
        super().__init__(name)
        self.current_room = current_room
        self.lantern_on = False
        self.world = world

    def __str__(self):
        return f"----------\n\nCurrent Location:\nRoom: {self.current_room.name}\nDescription: {self.current_room.get_desc(self.lantern_on)}\n=========="

    def __check_can_move(self, direction):
        try:
            room_events = self.world.events[self.current_room[direction].name]
        except:
            room_events = None
        if room_events is not None:
            if room_events["can_enter"]:
                return True
            else:
                print(room_events["locked_message"])
                return False
        else:
            return True

    def move(self, direction):
        if self.current_room[direction] is not None:
            if self.__check_can_move(direction):
                self.current_room = self.current_room[direction]
                print("You've arrived at...")
        else:
            print("Cannot go that way.")

    def give(self, item):
        super().give(item)
        item.on_take(self)

    def drop(self, item_name):
        item = self._find_item(item_name)
        if item is not None:
            if item.name == "lantern":
                print("I shouldn't drop this.")
            else:
                self.current_room.give(item)
                item.on_drop(self, self.current_room.name)
                self._delete_item(item)
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
            item = self._find_item(item_name)
            if item is not None:
                print(item.description)
            else:
                print(f"You checked your bag for [{item_name}] but found none.")

    def use(self, item_name):
        item = self._find_item(item_name)
        if item is not None:
            if item.name == "lantern":
                self.lantern_on = not self.lantern_on
                print(f"You turned {'on' if self.lantern_on else 'off' } the lantern.")
            if item.name == "key":
                self.world.unlock(self.current_room.name)
        else:
            print(f"You checked your bag for [{item_name}] but found none.")