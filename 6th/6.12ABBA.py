"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def count_abbas(text):
    """Waterloo mamma mia jeejee."""
    rnd = 0
    count = 0
    length = len(text)
    while rnd < length - 3:
        if text[rnd] == "a" and text[rnd+1] == "b" and text[rnd+2] == "b" and text[rnd+3] == "a":
            count += 1
        rnd += 1
    return count


def main():
    count = count_abbas(str(input("")))
    print(count)


if __name__ == "__main__":
    main()
