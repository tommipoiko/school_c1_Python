"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def main():
    print("Give 5 numbers:")
    first = int(input("Next number: "))
    second = int(input("Next number: "))
    third = int(input("Next number: "))
    fourth = int(input("Next number: "))
    fifth = int(input("Next number: "))
    numbers = [first, second, third, fourth, fifth]
    print("The numbers you entered, in reverse order:")
    rnd = 1
    while rnd <= 5:
        print(numbers[5-rnd])
        rnd += 1


if __name__ == "__main__":
    main()
