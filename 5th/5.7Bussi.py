"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def main():
    timetable = [630, 1015, 1415, 1620, 1720, 2000, 630, 1015, 1415, 1620, 1720, 2000]
    time = int(input("Enter the time (as an integer): "))
    print("The next buses leave:")
    rnd = 0
    if time > timetable[5]:
        time = 0
    while time > timetable[rnd]:
        rnd += 1
    tot = rnd + 2
    while rnd <= tot:
        print(timetable[rnd])
        rnd += 1


if __name__ == "__main__":
    main()
