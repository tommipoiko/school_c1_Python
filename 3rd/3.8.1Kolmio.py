"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


from math import sqrt


def area(a, b, c):
    """Funktio laskee kolmion pinta-alan halutuilla sivunmitoilla."""
    s = (a+b+c)/2
    return sqrt(s*(s-a)*(s-b)*(s-c))


def main():
    a = float(input("Enter the length of the first side: "))
    b = float(input("Enter the length of the second side: "))
    c = float(input("Enter the length of the third side: "))
    area(a, b, c)

    print(f"The triangle's area is {area(a, b, c):.1f}")


if __name__ == "__main__":
    main()
