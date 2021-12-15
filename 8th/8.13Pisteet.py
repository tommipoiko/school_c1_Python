"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def main():
    filename = input("Enter the name of the score file: ")
    try:
        file = open(filename, mode="r")
    except OSError:
        print("There was an error in reading the file.")
        return
    comp = file.readlines()
    total = dict()
    try:
        for mem in comp:
            div = mem.split()
            total[div[0]] = 0
        try:
            for mem in comp:
                div = mem.split()
                total[div[0]] += int(div[1])
        except ValueError:
            print("There was an erroneous score in the file:")
            print(f"{div[1]}")
            return
    except IndexError:
        print("There was an erroneous line in the file:")
        mem = mem.rstrip()
        print(mem)
        return
    print("Contestant score:")
    for word in sorted(total):
        print(f"{word} {total[word]}")


if __name__ == "__main__":
    main()
