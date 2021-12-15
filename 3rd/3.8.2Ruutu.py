"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def print_box(width, height, mark):
    """Tulostaa halutun neliön."""
    rnd = 1
    while rnd <= height:
        print(f"{mark}" * width)
        rnd += 1


def read_input(num):
    """Tarkistaa ilmoitetun arvon pitävyyden."""
    nro = input(num)
    while int(nro) < 1:
        nro = input(num)
    return int(nro)


def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
