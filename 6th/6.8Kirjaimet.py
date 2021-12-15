"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def capitalize_initial_letters(word):
    """Capitalizes the first letter of each word in a sentence etc."""
    x = word.title()
    return x


def main():
    x = capitalize_initial_letters(str(input("")))
    print(x)


if __name__ == "__main__":
    main()
