"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def main():
    filename = input("Enter the name of the file: ")
    file = open(filename, mode="r")
    rnd = 1
    for line in file:
        line = line.rstrip()
        print(rnd, line)
        rnd += 1


if __name__ == "__main__":
    main()
