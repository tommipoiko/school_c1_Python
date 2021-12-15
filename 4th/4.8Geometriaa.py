"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""

from math import pi

def square_input(side):
    """Tarkistaa neliön sivumitan arvon."""
    while side <= 0:
        side = float(input("Enter the length of the square's side: "))
    return side

def square_calc(side):
    """Laskee neliön geometriset mitat ilmoitetun sivumitan avulla."""
    circ = 4 * side
    area = side ** 2
    print(f"The circumference is {circ:.2f}")
    print(f"The surface area is {area:.2f}")

def rectangle_input1(side1):
    """Vaikuttaa siltä, että tekisi jotain, mutta ei tee."""
    return side1

def rectangle_input2(side2):
    """Vaikuttaa siltä, että tekisi jotain, mutta ei tee."""
    return side2

def rectangle_calc(side1, side2):
    """Laskee rectanglen geometriset arvot."""
    circR = 2 * side1 + 2 * side2
    areaR = side1 * side2
    print(f"The circumference is {circR:.2f}")
    print(f"The surface area is {areaR:.2f}")

def circle_input(radius):
    """Tarkistaa ympyrän säteen arvon pitävyyden."""
    while radius <= 0:
        radius = float(input("Enter the circle's radius: "))
    return radius

def circle_calc(radius):
    """Laskee ympyrän geometriset arvot säteen avulla."""
    circC = 2 * pi * radius
    areaC = pi * radius ** 2
    print(f"The circumference is {circC:.2f}")
    print(f"The surface area is {areaC:.2f}")

def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            side = float(input("Enter the length of the square's side: "))
            square_calc(square_input(side))

        elif answer == "r":
            side1 = float(input("Enter the length of the rectangle's side 1: "))
            while side1 <= 0:
                side1 = float(input("Enter the length of the rectangle's side 1: "))
            rectangle_input1(side1)
            side2 = float(input("Enter the length of the rectangle's side 2: "))
            while side2 <= 0:
                side2 = float(input("Enter the length of the rectangle's side 2: "))
            rectangle_input2(side2)
            rectangle_calc(side1, side2)

        elif answer == "c":
            radius = float(input("Enter the circle's radius: "))
            circle_calc(circle_input(radius))

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()

def main():
    menu()
    print("Goodbye!")

if __name__ == "__main__":
    main()
