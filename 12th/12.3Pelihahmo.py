"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


class Character:
    def __init__(self, name):
        """
        :param name: The characters name.
        Also defines the characters inventory.
        """
        self.__name = name
        self.__inventory = dict()

    def give_item(self, item_name):
        """
        :param item_name: The name of the item to be added
        to the characters inventory.
        """
        if item_name not in self.__inventory:
            self.__inventory[item_name] = 1
        else:
            self.__inventory[item_name] += 1

    def remove_item(self, item_name):
        """
        :param item_name: The name of the item to be removed from
        the characters inventory.
        """
        if item_name not in self.__inventory:
            return
        else:
            self.__inventory[item_name] -= 1

    def printout(self):
        """
        Prints all the data that a character possesses.
        """
        print(f"Name: {self.__name}")
        ctr = 0
        for item_name in sorted(self.__inventory):
            if self.__inventory[item_name] > 0:
                print(f"  {self.__inventory[item_name]} {item_name}")
                ctr += 1
        if ctr == 0:
            print("  --nothing--")

    def get_name(self):
        """
        :return: The characters name.
        """
        return self.__name

    def has_item(self, item_name):
        """
        :param item_name: The name of the item to
        be inspected.
        :return: True, if the item is held or False,
        if the item is not held.
        """
        if item_name in self.__inventory and self.__inventory[item_name] > 0:
            return True
        else:
            return False

    def how_many(self, item_name):
        """
        :param item_name: The name of the item to be
        inspected.
        :return: The amount of the items held.
        """
        if item_name in self.__inventory and self.__inventory[item_name] > 0:
            return self.__inventory[item_name]
        else:
            return 0


def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun",
                          "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
