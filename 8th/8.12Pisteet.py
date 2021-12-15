"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def main():
    filename = input("Enter the name of the score file: ")
    file = open(filename, mode="r")
    comp = file.readlines()
    total = dict()
    for mem in comp:
        div = mem.split()
        total[div[0]] = 0
    for mem in comp:
        div = mem.split()
        total[div[0]] += int(div[1])
    print("Contestant score:")
    for word in sorted(total):
        print(f"{word} {total[word]}")


if __name__ == "__main__":
    main()
