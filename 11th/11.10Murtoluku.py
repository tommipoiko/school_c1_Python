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
        self.__numerator = self.__numerator / greatest_common_divisor(nume,
                                                                      deno)
        self.__denominator = self.__denominator / greatest_common_divisor(nume,
                                                                          deno)
        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator):.0f}/{abs(self.__denominator):.0f}"

    def __str__(self):
        """
        :return: Info as text.
        """
        return f"{self.__numerator}/{self.__denominator}"

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

    def multiply(self, mod):
        """
        :param mod: Big numbrah.
        :return: My dad hopefully.
        """

        upper, lower = mod.filler()
        new_nume = upper * self.__numerator
        new_deno = lower * self.__denominator

        return Fraction(new_nume, new_deno)

    def filler(self):
        """
        :return: Aint it cool bro?
        """

        upper = self.__numerator
        lower = self.__denominator

        return upper, lower


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


def read_command(cmd, fractions):
    """
    :param cmd: Entered commandddd.
    :return: Blabalabababab.
    """

    while True:
        if cmd == "add":
            fractions = command_add(fractions)
            cmd = input("> ")
        elif cmd == "print":
            command_print(fractions)
            cmd = input("> ")
        elif cmd == "list":
            command_list(fractions)
            cmd = input("> ")
        elif cmd == "*":
            command_multiply(fractions)
            cmd = input("> ")
        elif cmd == "file":
            command_file(fractions)
            cmd = input("> ")
        elif cmd == "quit":
            print("Bye bye!")
            return
        else:
            print("Unknown command!")
            cmd = input("> ")


def command_file(fractions):
    """
    :param fractions: I'm too old for this shit.
    :return: Ur momma HA GOT EM'!
    """
    file_name = input("Enter the name of the file: ")
    if read_file(file_name) is not None:
        temporary = read_file(file_name)
        for name in temporary:
            try:
                parts = temporary[name].split("/")
                upper = int(parts[0])
                lower = int(parts[1])
                fractions[name] = Fraction(upper, lower)
            except IndexError:
                print("Error: the file cannot be read.")
                break
    return fractions


def read_file(filename):
    """
    :param filename: Haha.
    :return: Hihi.
    """

    temporary = dict()
    try:
        file = open(filename, mode="r")
        for row in file:
            items = row.split("=")
            temporary[items[0]] = items[1]
        return temporary

    except IndexError:
        print("Error in file!")
        return None

    except IOError:
        print("Error: the file cannot be read.")
        return None


def command_multiply(fractions):
    """
    :param fractions: Wuuhuu.
    :return: Jajaj.
    """
    first = input("1st operand: ")
    if first not in fractions:
        print(f"Name {first} was not found")
        return
    second = input("2nd operand: ")
    if second not in fractions:
        print(f"Name {second} was not found")
        return
    product = fractions[first].multiply(fractions[second])
    print(f"{fractions[first]} * {fractions[second]} = {product}")
    print(f"simplified {product.simplify()}")


def command_list(fractions):
    """
    :param fractions: Still the same.
    :return: Didn't change.
    """

    for i in sorted(fractions):
        print(f"{i} = {fractions[i]}")


def command_print(fractions):
    """
    :param fractions: Jababoey.
    :return: Pizza.
    """
    wanted = input("Enter a name: ")

    if wanted in fractions:
        print(f"{wanted} = {fractions[wanted]}")
    else:
        print(f"Name {wanted} was not found")


def command_add(fractions):
    """
    :param fractions: Jaja
    :return: Wuhuu
    """

    frac = input("Enter a fraction in the form integer/integer: ")
    name = input("Enter a name: ")
    parts = frac.split("/")
    upper = int(parts[0])
    lower = int(parts[1])
    fractions[name] = Fraction(upper, lower)

    return fractions


def main():
    fractions = dict()
    read_command(input("> "), fractions)


if __name__ == "__main__":
    main()
