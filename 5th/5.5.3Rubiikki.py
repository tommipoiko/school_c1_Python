"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def main():
    times = []
    rnd = 1
    while rnd <= 5:
        time = float(input(f"Enter the time for performance {rnd:}: "))
        times.append(time)
        rnd += 1
    times.remove(max(times))
    times.remove(min(times))
    avg = (times[0]+times[1]+times[2])/3
    print(f"The official competition score is {avg:.2f} seconds.")


if __name__ == "__main__":
    main()
