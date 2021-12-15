"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def read_file(filename):
    """Kommentti, että mitä tää tekee ja sitä rataa!"""
    info = dict()
    try:
        file = open(filename, mode="r")
        for unit in file:
            num = 1
            keys = unit.split(";")
            keys[-1] = keys[-1].strip()
            num += 1
            if num != 1:
                break
        for unit in file:
            items = unit.split(";")
            items[-1] = items[-1].strip()
            info[items[0]] = dict()
            rnd = 1
            while rnd < 5:
                info[items[0]][keys[rnd]] = items[rnd]
                rnd += 1
        return info

    except ValueError:
        return None
    except IOError:
        return None


def main():
    filename = "contacts.csv"
    info = read_file(filename)
    name = input("Enter the contact name: ")
    want = input("What do you need to know about the contact: ")
    print(info[name][want])


if __name__ == "__main__":
    main()
