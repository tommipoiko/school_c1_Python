"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def __lt__(self, other):
        """
        :param other: Something
        :return: Amazing values
        """

        upper, lower = other.filler()

        if self.__numerator / self.__denominator < upper / lower:
            return True
        else:
            return False

    def __gt__(self, other):
        """
        :param other: Same as before
        :return: Still the same numbdumb
        """

        upper, lower = other.filler()

        if self.__numerator / self.__denominator > upper / lower:
            return True
        else:
            return False

    def filler(self):
        """
        :return: Aint it cool bro?
        """

        upper = self.__numerator
        lower = self.__denominator

        return upper, lower

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator):.0f}/{abs(self.__denominator):.0f}"

    def simplify(self):
        """
        :return: Yo mama lol get rekt.
        """
        nume = self.__numerator
        deno = self.__denominator
        self.__numerator = self.__numerator / greatest_common_divisor(nume, deno)
        self.__denominator = self.__denominator / greatest_common_divisor(nume, deno)