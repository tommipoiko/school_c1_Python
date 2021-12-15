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

    def complement(self):
        """
        :return: Blaaaaaaaaaaaa vittu perkele.
        """

        if self.__numerator / self.__denominator < 0:
            new_nume = abs(self.__numerator)
            new_deno = abs(self.__denominator)
        else:
            new_nume = 0 - abs(self.__numerator)
            new_deno = abs(self.__denominator)

        return Fraction(new_nume, new_deno)

    def reciprocal(self):
        """
        :return: Pizza is muscle fuel - Iso-Tommi 2k21
        """

        if self.__numerator / self.__denominator < 0:
            new_nume = 0 - abs(self.__denominator)
            new_deno = abs(self.__numerator)
        else:
            new_nume = abs(self.__denominator)
            new_deno = abs(self.__numerator)

        return Fraction(new_nume, new_deno)

    def multiply(self, mod):
        """
        :param mod: Big numbrah.
        :return: My dad hopefully.
        """

        upper, lower = mod.filler()
        new_nume = upper * self.__numerator
        new_deno = lower * self.__denominator

        return Fraction(new_nume, new_deno)

    def divide(self, mod):
        """
        :param mod: The divider.
        :return: The great Cthulu.
        """

        upper, lower = mod.filler()
        new_nume = lower * self.__numerator
        new_deno = upper * self.__denominator

        return Fraction(new_nume, new_deno)

    def add(self, mod):
        """
        :param mod: Cool calzone mon.
        :return: Some weed bro.
        """

        upper, lower = mod.filler()
        new_nume = self.__numerator * lower + upper * self.__denominator
        new_deno = self.__denominator * lower

        return Fraction(new_nume, new_deno)

    def deduct(self, mod):
        """
        :param mod: Epic shit.
        :return: Even more epic!!
        """

        upper, lower = mod.filler()
        new_nume = self.__numerator * lower - upper * self.__denominator
        new_deno = self.__denominator * lower

        return Fraction(new_nume, new_deno)

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

    def __str__(self):
        """
        :return: Info as text.
        """
        return f"{self.__numerator}/{self.__denominator}"


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a
