"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def main():
    pass

    nro = input("Choose a number: ")
    num = int(nro)
    rep = 1
    while rep <= 10:
        multi = (rep)*(num)
        print(rep, "*", num, "=", multi)
        rep += 1

if __name__ == "__main__":
    main()
