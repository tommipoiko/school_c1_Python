"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def main():
    pass

    num=input("How many numbers would you like to have? ")
    tot=int(num)
    choise=1
    round=int(choise)
    while round <= tot:
        if round%3 == 0 and round%7 ==0:
            print("zip boing")
            round += 1
        elif round%7 == 0:
            print("boing")
            round += 1
        elif round%3 == 0:
            print("zip")
            round += 1
        else:
            print(round)
            round += 1

if __name__ == "__main__":
    main()
