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
        print(f"{mark}"*width)
        rnd += 1


def main():
    width = int(input("Enter the width of a frame: "))
    height = int(input("Enter the height of a frame: "))
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
