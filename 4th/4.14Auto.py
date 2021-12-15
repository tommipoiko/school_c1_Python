"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""

from math import sqrt


def menu():
    """This is the menu of the car application Do not change anything in this."""

    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size
    gas_consumption = read_number("How many liters of gas does the car " +
                                  "consume per hundred kilometers? ")
    x = 0.0
    y = 0.0

    while True:
        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, gas))

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            gas = fill(tank_size, to_fill, gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            (gas, x, y) = drive(x, y, new_x, new_y, gas, gas_consumption)

        elif choice == "3":
            break

    print("Thank you and bye!")


def fill(tank_size, to_fill, gas):
    """This function has three parameters which are all FLOATs:
      (1) the size of the tank
      (2) the amount of gas that is requested to be filled in
      (3) the amount of gas in the tank currently"""

    space = tank_size - gas
    if space >= to_fill:
        gas += to_fill
    else:
        gas = tank_size
    return gas


def drive(x, y, new_x, new_y, gas, gas_consumption):
    """This function has six parameters. They are all floats.
      (1) The current x coordinate
      (2) The current y coordinate
      (3) The destination x coordinate
      (4) The destination y coordinate
      (5) The amount of gas in the tank currently
      (6) The consumption of gas per 100 km of the car
    The parameters have to be in this order.
    The function returns three floats:
      (1) The amount of gas in the tank AFTER the driving
      (2) The reached (new) x coordinate
      (3) The reached (new) y coordinate"""

    distance = sqrt((new_x - x) ** 2 + (new_y - y) ** 2)
    short = travel_check(gas, gas_consumption, distance)
    x += (new_x - x) * short
    y += (new_y - y) * short
    gas = gas_check(gas, gas_consumption, distance)
    return gas, x, y


def gas_check(gas, gas_consumption, distance):
    """Checks the amount of gas in the tank."""
    if (gas_consumption / 100 * distance) < gas:
        gas = gas - gas_consumption / 100 * distance
    else:
        gas = 0
    return gas


def travel_check(gas, gas_consumption, distance):
    """Checks if the gas is enough for the wanted trip."""
    consumed = (gas_consumption / 100 * distance)
    if consumed > gas:
        short = gas / consumed
    else:
        short = 1.0
    return short


def read_number(prompt, error_message="Incorrect input!"):
    """
    DO NOT TOUCH THIS FUNCTION.
    This function reads input from the user.
    Also, don't worry if you don't understand it.
    """

    try:
        return float(input(prompt))

    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()


if __name__ == "__main__":
    main()
