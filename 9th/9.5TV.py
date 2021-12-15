"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def read_file(filename):
    """
    Reads and saves the series and their genres from the file. And gets the
    party started oh yeah!
    """

    programs = dict()

    try:
        file = open(filename, mode="r")

        for row in file:
            name, genres = row.rstrip().split(";")

            genres = genres.split(",")

            programs[name] = genres

        file.close()
        return programs

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")

    genre_data = read_file(filename)

    choices = []
    for name in genre_data:
        for one in genre_data[name]:
            if one not in choices:
                choices.append(one)

    text = ""
    for i in sorted(choices):
        text += i + " "
    text = text.rstrip()
    text = text.replace(" ", ", ")
    print(f"Available genres are: {text}")

    while True:
        genre = input("> ")

        if genre == "exit":
            return

        results = []

        for name in genre_data:
            for one in genre_data[name]:
                if one == genre:
                    results.append(name)

        for i in sorted(results):
            print(i)


if __name__ == "__main__":
    main()
