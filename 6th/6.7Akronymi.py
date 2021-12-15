"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def create_an_acronym(name):
    """Creates an acronym out of a given name. Returns the acronym."""
    words = name.split(" ")
    amount = len(words)
    rnd = 0
    acronym = ""
    while rnd < amount:
        acronym += words[rnd][0]
        rnd += 1
    acronym = acronym.upper()

    return acronym


def main():
    acronym = create_an_acronym(input(""))
    print(acronym)


if __name__ == "__main__":
    main()
