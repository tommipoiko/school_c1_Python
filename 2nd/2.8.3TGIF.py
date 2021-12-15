"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def main():
    pass

    day=int(3)
    month=int(1)

    while day <= 31:
        print(f"{day}.{month}.")
        day += 7
    month += 1
    day=int(0)

    while day < 28:
        day += 7
        print(f"{day}.{month}.")
    month += 1
    day=int(0)

    while day < 28:
        day += 7
        print(f"{day}.{month}.")
    month += 1
    day=day-31+7

    while day <= 30:
        print(f"{day}.{month}.")
        day += 7
    month += 1
    day=day-30

    while day <= 31:
        print(f"{day}.{month}.")
        day += 7
    month += 1
    day=day-31

    while day <= 30:
        print(f"{day}.{month}.")
        day += 7
    month += 1
    day=day-30

    while day <= 31:
        print(f"{day}.{month}.")
        day += 7
    month += 1
    day=day-31

    while day <= 31:
        print(f"{day}.{month}.")
        day += 7
    month += 1
    day=day-31

    while day <= 30:
        print(f"{day}.{month}.")
        day += 7
    month += 1
    day=day-30

    while day <= 31:
        print(f"{day}.{month}.")
        day += 7
    month += 1
    day=day-31

    while day <= 30:
        print(f"{day}.{month}.")
        day += 7
    month += 1
    day=day-30

    while day <= 31:
        print(f"{day}.{month}.")
        day += 7
    month += 1
    day=day-31+7

if __name__ == "__main__":
    main()
