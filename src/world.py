class World:
    def __init__(self):
        self.events = {
            "Foyer": {
                "can_enter": True,
                "event_type": "unlock",
                "event_target": "Stairwell",
                "requires": "key"
            },
            "Stairwell": {
                "can_enter": False,
                "locked_message": "The passage is barred by a locked gate.",
                "unlocked_message": "You used the key to unlock the gate.",
                }
        }

    def trigger(self, room_name, item_name):
        try:
            target = self.events[self.events[room_name]["event_target"]]
            item = self.events[room_name]["requires"]
            event = self.events[room_name]["event_type"]
            if item_name == item:
                if event == "unlock":
                    target["can_enter"] = True
                    print(target["unlocked_message"])
            else:
                print("Can't use that here")
        except:
            print("Can't use that here")