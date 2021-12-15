"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def calculate_angle(angle1, angle2=90):
    """Laskee kolmannen kulman suuruuden."""
    return 180 - angle1 - angle2

def main():
    calculate_angle(angle1, angle2)

if __name__ == "__main__":
    main()
