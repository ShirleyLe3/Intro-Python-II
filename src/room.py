from item_container import ItemContainer

class Room(ItemContainer):
    def __init__(self, name, description, items, dark=False):
        super().__init__(name, items)
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.dark = dark

    def __getitem__(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "e":
            return self.e_to
        elif direction == "s":
            return self.s_to
        elif direction == "w":
            return self.w_to

    def get_desc(self, lantern_on):
        if self.dark and not lantern_on:
            return "The room is too dark to see anything."
        else:
            return self.description

    def look(self, lantern_on):
        text = "You look around and see...\n"
        if self.n_to is not None:
            text += f"North: {self.n_to.name}\n"
        if self.e_to is not None:
            text += f"East: {self.e_to.name}\n"
        if self.s_to is not None:
            text += f"South: {self.s_to.name}\n"
        if self.w_to is not None:
            text += f"West: {self.w_to.name}\n"
        if self.dark and not lantern_on:
            text += "The room is too dark to see anything else."
        else:
            if len(self.items) > 0:
                for item in self.items:
                    text += f"{item.description}\n"
        print(text.rstrip())

    def take(self, item_name, player):
        item = self._find_item(item_name)
        if item is not None and ((not self.dark) or (player.lantern_on)):
            player.give(item)
            self._delete_item(item)
        else:
            print(f"You looked around for [{item_name}] but found none.")