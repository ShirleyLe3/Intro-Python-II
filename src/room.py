# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
    def __getitem__(self, direction):
        if direction == 'n':
            return self.n_to
        elif direction == 'e':
            return self.e_to
        elif direction == 's':
            return self.s_to
        elif direction == 'w':
            return self.w_to
    def look(self):
        text = 'You look around and see...\n'
        if self.n_to is not None:
            text += f'North: {self.n_to.name}\n'
        if self.e_to is not None:
            text += f'East: {self.e_to.name}\n'
        if self.s_to is not None:
            text += f'South: {self.s_to.name}\n'
        if self.w_to is not None:
            text += f'West: {self.w_to.name}\n'
        if len(self.items) > 0:
            for item in self.items:
                text += f'{item.description}\n'
        print(text)
    def take(self, item_name, player):
        found = False
        for i, item in enumerate(self.items):
            if item.name == item_name:
                player.give(item)
                del self.items[i]
                found = True
        if not found:
            print(f'You looked around for [{item_name}] but found none.')
    def give(self, item):
        self.items.append(item)
        print(f'You dropped [{item.name}] in {self.name}')