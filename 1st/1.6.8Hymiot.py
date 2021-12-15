"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def main():
    pass

    fiilis=input("How do you feel? (1-10) ")
    feeling=int(fiilis)
    if feeling > 10 or feeling < 1:
        print("Bad input!")
    elif feeling == 10:
        print("A suitable smiley would be :-D")
    elif feeling > 7:
        print("A suitable smiley would be :-)")
    elif feeling > 3:
        print("A suitable smiley would be :-|")
    elif feeling == 1:
        print("A suitable smiley would be :'(")
    else:
        print("A suitable smiley would be :-(")

if __name__ == "__main__":
    main()
