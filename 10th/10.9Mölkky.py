"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


class Player:
    """
    The name is Bond, James Bond and I'm here to fry some pizza.
    """

    def __init__(self, name):
        """
        :param name: The players name.
        """

        self.__name = name
        self.__points = 0
        self.__throws = 0
        self.__avg = 0
        self.__percentage = 0
        self.__counter = 0
        self.__setback = 0

    def get_name(self):
        """
        :return: Returns the name of the big guy.
        """

        return self.__name

    def add_points(self, pts):
        """
        :param pts: The amount of points to be added.
        :return: Dunno lol.
        """

        self.__points += pts
        self.__throws += 1

        if pts > 0:
            self.__counter += 1

        if 50 - self.__points < 11 and self.__points < 50:
            print(f"{self.__name} needs only {50 - self.__points} "
                  f"points. It's better to avoid knocking down the pins with "
                  f"higher points.")
        if self.__points > 50:
            print(f"{self.__name} gets penalty points!")
            self.__points = 25
            self.__setback = 1

    def calc_avg(self, pts):
        """
        :param pts: Required to inspect the relation to the avg.
        :return: None kys.
        """
        self.__avg = self.__points / self.__throws
        if pts > self.__avg and self.__setback == 0:
            print(f"Cheers {self.__name}!")
        else:
            self.__setback = 0

    def has_won(self):
        """
        :return: Is there a winner or not lol get a brain numbdumb.
        """

        if self.__points == 50:
            return True
        else:
            return False

    def get_points(self):
        """
        :return: Amount of points.
        """

        return self.__points

    def get_perc(self):
        """
        :return: The percentage.
        """
        if self.__throws == 0:
            percentage = self.__counter / 1 * 100
        else:
            percentage = self.__counter / self.__throws * 100

        return percentage


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        in_turn.calc_avg(pts)

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p" + f", hit percentage {player1.get_perc():.1f}")
        print(player2.get_name() + ":", player2.get_points(), "p" + f", hit percentage {player2.get_perc():.1f}")
        print("")

        throw += 1


if __name__ == "__main__":
    main()
