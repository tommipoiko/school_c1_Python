"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def main():
    pass

    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i * j:>4}", end="")
        print()

if __name__ == "__main__":
    main()