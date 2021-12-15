"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def read_file(filename):
    """
    :param filename: Muuttuja on merkkijono. Tätä käytetään halutun tiedoston
    avaamiseen.
    :return: Funktio palauttaa kirjaston, jonka sisällä on kirjasto. Tämän
    nimi on course_info ja tätä käytetään koko ohjelmassa.
    """

    course_info = dict()
    try:
        print("")
        file = open(filename, mode="r")
        for row in file:
            items = row.split(";")
            items[-1] = items[-1].strip()
            if items[0] not in course_info:     # items[0] kuvaa laitoksen
                                                # nimeä, kuten fysiikka tai
                                                # kemia.
                course_info[items[0]] = dict()
            course_info[items[0]][items[1]] = items[2]
        if len(items) > 3:
            print("Error in file!")
            return None
        return course_info

    except IndexError:
        print("Error in file!")
        return None

    except IOError:
        print("Error opening file!")
        return None


def check_input(command, course_info):
    """
    :param command: Merkkijono, joka jaetaan listan osiksi ja tämän avulla
    suoritetaan haluttuja toimintoja ohjelmassa.
    :param course_info: Kirjasto kirjastossa, jossa on halutut tiedot.
    """

    list_of_commands = ["A", "a", "C", "c", "D", "d",
                        "P", "p", "R", "r", "Q", "q"]

    command = command.split()

    while True:

        while command[0] not in list_of_commands:
            print("Invalid command!")
            print("")
            print("[A]dd / [C]redits / [D]elete / [P]rint all / p[R]int "
                  "department / [Q]uit")
            command = input("Enter command: ")
            print("")
            command = command.split()

        while command[0] in list_of_commands:

            #Komennon oikeellisuuden tarkistettua suoritetaan vastaava funktio.

            if command[0] == "P" or command[0] == "p":
                print_all(course_info)

            if command[0] == "R" or command[0] == "r":
                print_department(command, course_info)

            if command[0] == "C" or command[0] == "c":
                amount_of_credits(command, course_info)

            if command[0] == "A" or command[0] == "a":
                course_info = add_to_courses(command, course_info)

            if command[0] == "D" or command[0] == "d":
                course_info = delete_course(command, course_info)

            if command[0] == "Q" or command[0] == "q":
                print("")
                print("Ending program.")
                return

            print("")
            print("[A]dd / [C]redits / [D]elete / [P]rint all / p[R]int "
                  "department / [Q]uit")
            command = input("Enter command: ")
            print("")
            command = command.split()


def print_all(course_info):
    """
    :param course_info: Kirjasto kirjastossa, jossa on halutut tiedot.
    """

    for departments in sorted(course_info.keys()):
        print(f"*{departments}*")
        courses = sorted(course_info[departments])
        for course in courses:
            print(f"{course} : {course_info[departments][course]} cr")


def print_department(command, course_info):
    """
    :param command: Haluttu toiminto komentona jaettu listan osiksi.
    :param course_info: Kirjasto kirjastossa, jossa on halutut tiedot.
    """

    if command[1] in course_info:
        print("")
        for departments in sorted(course_info.keys()):
            if departments == command[1]:
                print(f"*{departments}*")
                courses = sorted(course_info[departments])
                for course in courses:
                    print(f"{course} : {course_info[departments][course]} cr")
    else:
        print("Department not found!")


def amount_of_credits(command, course_info):
    """
    :param command: Haluttu toiminto komentona jaettu listan osiksi.
    :param course_info: Kirjasto kirjastossa, jossa on halutut tiedot.
    """

    sum_of_credits = int(0)

    if command[1] in course_info:
        for departments in sorted(course_info.keys()):
            if departments == command[1]:
                for course in course_info[departments]:
                    sum_of_credits += int(course_info[departments][course])
                print(f"Department {departments} has to offer {sum_of_credits} cr.")
    else:
        print("Department not found!")


def add_to_courses(command, course_info):
    """
    :param command: Haluttu toiminto komentona jaettu listan osiksi.
    :param course_info: Kirjasto kirjastossa, jossa on halutut tiedot.
    :return: Palauttaa muokatun course_info -kirjaston uuteen käyttöön.
    """

    new_course_name = ""
    print("")
    for unit in command[2:len(command) - 1]:
        new_course_name += str(unit) + " "
    new_course_name = new_course_name.rstrip()

    if command[1] in course_info and len(command) > 2:
        credits_amount = command[len(command)-1]
        course_info[command[1]][new_course_name] = credits_amount
        print(f"Added course {new_course_name} to department {command[1]}")

    elif command[1] not in course_info and len(command) > 2:
        course_info[command[1]] = dict()
        credits_amount = command[len(command) - 1]
        course_info[command[1]][new_course_name] = credits_amount
        print(f"Added department {command[1]} with course {new_course_name}")
    else:
        print("Invalid command!")

    return course_info


def delete_course(command, course_info):
    """
    :param command: Haluttu toiminto komentona jaettu listan osiksi.
    :param course_info: Kirjasto kirjastossa, jossa on halutut tiedot.
    :return: Palauttaa muokatun course_info kirjaston uuteen käyttöön.
    """

    new_course_name = ""
    for unit in command[2:len(command)]:
        new_course_name += str(unit) + " "
    new_course_name = new_course_name.rstrip()

    if command[1] in course_info:
        if len(command) == 2:
            print("")
            print(f"Department {command[1]} removed.")
            del course_info[command[1]]

        elif len(command) > 2 and new_course_name in course_info[command[1]]:
            print("")
            print(f"Department {command[1]} course {new_course_name} removed.")
            del course_info[command[1]][new_course_name]

        else:
            print("")
            print(f"Course {new_course_name} from {command[1]} not found!")

    else:
        print("")
        print(f"Department {command[1]} not found!")

    return course_info


def main():
    course_info = read_file(input("Enter file name: "))
    if course_info is not None:
        print("[A]dd / [C]redits / [D]elete / [P]rint all / p[R]int "
              "department / [Q]uit")
        check_input(input("Enter command: "), course_info)


if __name__ == "__main__":
    main()
