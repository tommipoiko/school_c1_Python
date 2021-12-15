"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def main():
    pass

    ans=str(input("Bored? (y/n) "))
    if ans == "y" or ans == "Y":
        print("Well, let's stop this, then.")
    while ans != "y" and ans != "n" and ans != "Y" and ans != "N":
        print("Incorrect entry.")
        ans=str(input("Bored? (y/n) "))
        if ans == "y" or ans == "Y":
            print("Well, let's stop this, then.")
        while ans == "n" or ans == "N":
            if ans == "n" or ans == "N":
                ans=str(input("Bored? (y/n) "))
                if ans != "y" and ans != "n" and ans != "Y" and ans != "N":
                    print("Incorrect entry.")
                    ans=str(input("Bored? (y/n) "))
        if ans != "y" and ans != "n" and ans != "Y" and ans != "N":
            print("Incorrect entry.")
            ans=str(input("Bored? (y/n) "))
        if ans == "y" or ans == "Y":
            print("Well, let's stop this, then.")
    while ans == "n" or ans == "N":
        ans=str(input("Bored? (y/n) "))
        if ans == "y" or ans == "Y":
            print("Well, let's stop this, then.")

if __name__ == "__main__":
    main()
