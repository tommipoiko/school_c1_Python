"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def print_box(width, height, border_mark = "#", inner_mark = " "):
    """Piirtää laatikon tyylikkäästi."""
    count = 1
    while count <= height:
        if count == 1 or count == height:
            print(width*f"{border_mark}")
        if count != 1 and count != height:
            print(f"{border_mark}",(width-2)*f"{inner_mark}",f"{border_mark}", sep="")
        count += 1
    print("")

def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)

if __name__ == "__main__":
    main()
