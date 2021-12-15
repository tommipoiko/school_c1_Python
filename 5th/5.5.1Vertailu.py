"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def are_all_members_same(list):
    """Tarkistaa ovatko listan jäsenet samoja."""
    if list == []:
        return True
    else:
        if max(list) == min(list):
            return True
        else:
            return False


def main():
    are_all_members_same(list)


if __name__ == "__main__":
    main()
