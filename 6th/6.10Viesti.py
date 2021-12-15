"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def read_message():
    """Eeeppinen docstring tähän välii."""
    text = []
    given = str(input(""))
    if given != "":
        text.append(given)
    while len(given) > 0:
        given = str(input(""))
        if given != "":
            text.append(given)
    return text


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("The same, shouting:")
    for i in range(0, len(msg)):
        print(msg[i].upper())


if __name__ == "__main__":
    main()
