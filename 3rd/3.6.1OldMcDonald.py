"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def print_verse(anml, snd):
    """Funktio kirjoittaa laulun sanat halutuilla eläimillä ja äänillä."""
    print("Old MACDONALD had a farm")
    print("E-I-E-I-O")
    print(f"And on his farm he had a {anml}")
    print("E-I-E-I-O")
    print(f"With a {snd} {snd} here")
    print(f"And a {snd} {snd} there")
    print(f"Here a {snd}, there a {snd}")
    print(f"Everywhere a {snd} {snd}")
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")

def main():
    print_verse("cow", "moo")
    print()
    print_verse("pig", "oink")
    print()
    print_verse("duck", "quack")
    print()
    print_verse("horse", "neigh")
    print()
    print_verse("lamb", "baa")

if __name__ == "__main__":
    main()
