"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def input_to_list(amount):
    """Kysyy luvut jne jne joojoo."""
    numbers = []
    rnd = 1
    while rnd <= amount:
        numbers.append(int(input("")))
        rnd += 1
    return numbers


def main():
    amount = int(input("How many numbers do you want to process: "))
    print(f"Enter {amount} numbers:")
    numbers = input_to_list(amount)
    search = int(input("Enter the number to be searched: "))
    tick = 0
    for number in numbers:
        if number == search:
            tick += 1
    if tick != 0:
        print(f"{search} shows up {tick} times among the numbers you have entered.")
    else:
        print(f"{search} is not among the numbers you have entered.")


if __name__ == "__main__":
    main()
