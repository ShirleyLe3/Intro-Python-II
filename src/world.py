class World:
    def __init__(self):
        self.events = {
            "Foyer": {
                "can_enter": True,
                "unlock": "Stairwell"
            },
            "Stairwell": {
                "can_enter": False,
                "locked_message": "The passage is barred by a locked gate.",
                "unlocked_message": "You used the key to unlock the gate.",
                }
        }

    def unlock(self, room_name):
        try:
            room = self.events[self.events[room_name]["unlock"]]
            room["can_enter"] = True
            print(room["unlocked_message"])
        except:
            print("Can't use that here")