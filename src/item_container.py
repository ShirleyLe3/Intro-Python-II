class ItemContainer:
    def __init__(self, name, items=[]):
        self.name = name
        self.items = items

    def __find_item__(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    def __delete_item__(self, item):
        for i, my_item in enumerate(self.items):
            if my_item.name == item.name:
                del self.items[i]

    def give(self, item):
        self.items.append(item)