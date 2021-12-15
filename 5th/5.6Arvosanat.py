"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def convert_grades(grades):
    """Antaa rutto-oppilaille kivat arvosanat."""
    rnd = 0
    while rnd < len(grades):
        if grades[rnd] != 0:
            grades.insert(rnd, 6)
            grades.pop(rnd+1)
        rnd += 1


def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()
