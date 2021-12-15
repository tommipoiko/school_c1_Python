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
    print("The numbers you entered that were greater than zero were:")
    for number in numbers:
        if number > 0:
            print(number)

if __name__ == "__main__":
    main()
