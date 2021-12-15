"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def repeat_name(name, cntr):
    """Tulostaa karhujen nimeä halutun verran."""
    rnd = 1
    while rnd <= cntr:
        print(f"{name}, {name} Bear")
        rnd += 1


def verse(line, name):
    """Tulostaa laulun sanat."""
    print(f"{line}")
    print(f"{name}, {name}")
    print(f"{line}")
    repeat_name(name, 3)
    print(f"{line}")
    repeat_name(name, 1)



def main():
    verse("I know someone you don't know", "Yogi")
    print()
    verse("Yogi has a best friend too", "Boo Boo")
    print()
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()
