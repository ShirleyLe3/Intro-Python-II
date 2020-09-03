room_desc = {
    "outside": "North of you, the cave mount beckons",
    "foyer": """Dim light filters in from the south. Dusty
passages run north and east.""",
    "overlook": """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.
On the walls hang a few lanterns, dimly lighting the opening.""",
    "narrow": """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    "treasure": """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
}

def print_intro(name):
    print(f"""\n\nHello {name}! You have started your adventure.
Type the 'help' command for more information.

==========
At the start of your journey, you find yourself...""")