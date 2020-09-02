from room import Room
from player import Player
from item import Item

# Create items
items = {
    "key": Item("key", "A rusty old key."),
    "sword": Item("sword", "-A heavy, worn [sword]. Sharp enough."),
}

# Declare all the rooms
room = {
    "outside": Room(
        "Outside Cave Entrance",
        "North of you, the cave mount beckons",
        [items["sword"]],
    ),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
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
# name = input('Enter your name: ')
name = "Drew"
player = Player(name, room["outside"])
command = ""

# user actions
def do(command):
    command = command.strip()
    command = command.split(" ")

    if command[0] == "n" or command[0] == "e" or command[0] == "s" or command[0] == "w":
        player.move(command[0])
    if command[0] == "look":
        player.current_room.look()
    if command[0] == "take" or command[0] == "get":
        if len(command) > 1:
            player.current_room.take(command[1], player)
        else:
            print("Specify an item to take.")
    if command[0] == "drop":
        if len(command) > 1:
            player.drop(command[1])
        else:
            print("Specify an item to drop.")
    if command[0] == "i" or command[0] == "inventory" or command[0] == "bag":
        if len(command) > 1:
            player.bag(command[1])
        else:
            player.bag()

# game loop
while command != "q":
    print(f"\n{player}\n")
    command = input("Command: ")
    do(command)
