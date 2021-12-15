"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def write_text(big, line):
    """Kirjottaa sen tekstin oikeanlaisena. Toivottavasti ainakin."""
    round = 1
    rnd = 1
    while round < ((len(big)) // line + 1):
        query = ""
        while rnd <= (line * round):
            query += big[rnd - 1]
            rnd += 1
        print(query)
        round += 1
    query = ""
    while rnd < len(big):
        query += big[rnd - 1]
        rnd += 1
    print(query)


def analyze_text(msg):
    """Tää tekee kans jotai hauskaa. Väsyttää jo perkele."""
    text = ""
    for i in range(0, len(msg)-1):
        text += str(msg[i]) + " "
    text += str(msg[len(msg)-1])

    return text


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
    line = int(input("Enter the number of characters per line: "))
    big = analyze_text(msg)
    write_text(big, line)


if __name__ == "__main__":
    main()
