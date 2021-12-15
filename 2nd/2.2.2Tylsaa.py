"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def main():
    pass

    answer = input("Answer Y or N: ")
    while answer != "y" and answer != "n" and answer != "Y" and answer != "N":
        if answer != "y" and answer != "n" and answer != "Y" and answer != "N":
            print("Incorrect entry.")
            answer = input("Answer Y or N: ")
        else:
            print("You answered", answer)
    print("You answered", answer)

if __name__ == "__main__":
    main()