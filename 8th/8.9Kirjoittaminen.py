"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def main():
    filename = input("Enter the name of the file: ")
    try:
        save_file = open(filename, mode="w")
        print("Enter rows of text. Quit by entering an empty row.")
        rnd = 1
        while True:
            text_line = input()
            if text_line == "":
                break
            print(f"{rnd} {text_line}", file=save_file)
            rnd += 1
        save_file.close()
        print(f"File {filename} has been written.")
    except OSError:
        print(f"Writing the file {filename} was not successful.")


if __name__ == "__main__":
    main()
