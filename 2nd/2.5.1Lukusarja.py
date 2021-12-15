"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def main():
    pass

    start=int(1)
    end=int(input("How many numbers would you like to have? "))
    for number in range(start, end+1):
        if number%3==0 and number%7==0:
            print("zip boing")
        elif number%3==0:
            print("zip")
        elif number%7==0:
            print("boing")
        else:
            print(number)

if __name__ == "__main__":
    main()
