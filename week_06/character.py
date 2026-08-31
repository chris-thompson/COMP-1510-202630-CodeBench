"""
Nest data structures: a list of dictionaries and a dictionary of dictionaries.

A dictionary is a natural way to represent one game character. When we
need a whole party (group) of characters, we put the dictionaries in a
list. When we need to look users up by name, we put dictionaries inside
a dictionary.
"""


def create_character(name):
    """
    Create a new game character as a dictionary.

    :param name: a non-empty string
    :precondition: name is a non-empty string
    :return: a dictionary representing a level-one character with the
             keys "name", "level", "HP", "X", and "Y"

    >>> create_character('Alvin')
    {'name': 'Alvin', 'level': 1, 'HP': 10, 'X': 0, 'Y': 0}
    >>> create_character('M')
    {'name': 'M', 'level': 1, 'HP': 10, 'X': 0, 'Y': 0}
    """
    return {"name": name, "level": 1, "HP": 10, "X": 0, "Y": 0}


def main():
    """
    Drive the program.
    """
    # A list of dictionaries: a party of adventurers.
    cleric = create_character("Alvin")
    ranger = create_character("Marg")
    mage = create_character("Drucilla")
    party_of_adventurers = [cleric, ranger, mage]
    for adventurer in party_of_adventurers:
        print(adventurer["name"], "has", adventurer["HP"], "HP")

    # A dictionary of dictionaries: usernames are the keys, and each
    # value is another dictionary of information about that user.
    users = {
        "lester": {"first": "Lester", "last": "Pearson", "location": "Ottawa"},
        "kim": {"first": "Kim", "last": "Campbell",
                "location": "Port Alberni"},
    }
    for username, information in users.items():
        print(username, "lives in", information["location"])


if __name__ == "__main__":
    main()
