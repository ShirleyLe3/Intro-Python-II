class World:
    def __init__(self):
        self.events = {
            "Stairwell": {
                "can_enter": False,
                "locked_message": "The passage is barred by a locked gate.",
                "unlocked_message": "You used the key to unlock the gate.",
                }
        }

    def unlock(self, room_name):
        room = self.events[room_name]
        room.can_enter = True
        print(room)