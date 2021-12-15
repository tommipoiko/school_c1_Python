"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def compare_floats(A, B, EPSILON):
    """Tutkii, että ovatko kaksi lukua tarpeeksi lähellä toisiaan."""
    if abs(A-B) < EPSILON:
        return True
    else:
        return False

def main():
    pass

    compare_floats(A, B, EPSILON)

if __name__ == "__main__":
    main()
