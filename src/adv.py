import os
from room import Room
from player import Player
from item import Item
from room_desc import room_desc

# Create items
items = {
    "key": Item("key", "-A rusty old [key]."),
    "sword": Item("sword", "-A heavy, worn [sword]. Sharp enough."),
}

# Declare all the rooms
room = {
    "outside": Room(
        "Outside Cave Entrance",
        room_desc["outside"],
        [items["sword"]],
    ),
    "foyer": Room(
        "Foyer",
        room_desc["foyer"],
    ),
    "overlook": Room(
        "Grand Overlook",
        room_desc["overlook"],
    ),
    "narrow": Room(
        "Narrow Passage",
        room_desc["narrow"],
    ),
    "treasure": Room(
        "Treasure Chamber",
        room_desc["treasure"],
    ),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def get_help():
    cwd = os.getcwd()
    f = open(f"{cwd}\\src\\help.txt", "r")
    print(f.read())
    f.close()


name = input("Enter your name: ")
# name = "Drew"
player = Player(name, room["outside"])
command = ""
print(
    f"""\n\nHello {name}! You have started your adventure. Type the 'help' command for more information. At the start of your journey, you find yourself..."""
)
# user actions
def do(command):
    command = command.strip()
    command = command.split(" ")

    if command[0] == "n" or command[0] == "e" or command[0] == "s" or command[0] == "w":
        player.move(command[0])
    elif command[0] == "look":
        player.current_room.look()
    elif command[0] == "take" or command[0] == "get":
        if len(command) > 1:
            player.current_room.take(command[1], player)
        else:
            print("Specify an item to take.")
    elif command[0] == "drop":
        if len(command) > 1:
            player.drop(command[1])
        else:
            print("Specify an item to drop.")
    elif command[0] == "i" or command[0] == "inventory" or command[0] == "bag":
        if len(command) > 1:
            player.bag(command[1])
        else:
            player.bag()
    elif command[0] == "help":
        get_help()
    elif command[0] == "q":
        print(f"Goodbye {name}...")
    else:
        print("Invalid command. Type 'help' to see a list of commands.")


# game loop
while command != "q":
    print(f"\n{player}\n")
    command = input("Command: ")
    do(command)
