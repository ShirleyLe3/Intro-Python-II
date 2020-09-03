import os
from room import Room
from player import Player
from item import Item
from game_text import room_desc, print_intro

# Create items
items = {
    "key": Item("key", "-A rusty old [key]."),
    "sword": Item("sword", "-A heavy, worn [sword]. Sharp enough."),
    "lantern": Item("lantern", "-An oil [lantern]. This could be useful in dark places.")
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
        [],
        True
    ),
    "overlook": Room(
        "Grand Overlook",
        room_desc["overlook"],
        [items["lantern"]],
    ),
    "narrow": Room(
        "Narrow Passage",
        room_desc["narrow"],
        [],
        True
    ),
    "treasure": Room(
        "Treasure Chamber",
        room_desc["treasure"],
        [items["key"]],
        True
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


def get_help():
    cwd = os.getcwd()
    f = open(f"{cwd}\\src\\help.txt", "r")
    print(f.read())
    f.close()


# game start
name = input("Enter your name: ")
player = Player("Player", room["outside"])
command = ""
print_intro(name)


# user actions
def do(command):
    command = command.strip()
    command = command.split(" ")

    if command[0] == "n" or command[0] == "e" or command[0] == "s" or command[0] == "w":
        player.move(command[0])
    elif command[0] == "look":
        player.current_room.look(player.lantern_on)
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
    elif command[0] == "use":
        if len(command) > 1:
            player.use(command[1])
        else:
            print("Specify an item in your bag to use.")
    else:
        print("Invalid command. Type 'help' to see a list of commands.")


# game loop
while command != "q":
    print(f"\n{player}\n\n==========")
    command = input("Command: ")
    do(command)
