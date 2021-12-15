"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi

COMP1-Exam
"""


LOAN_TIME = 3
MAX_LOANS = 3


class Librarycard:
    def __init__(self, card_id, card_holder):
        self.__id = card_id
        self.__holder = card_holder
        self.__loans = {}

    def holder(self):
        return self.__holder

    def add_to_list(self, book_code):
        """
        Metodi katsoo, että löytyykö kirjaa jo lainasta ja
        suotuisassa tilanteessa lisää kirjan tunnuksensa
        piiriin lainaan. Metodi myös palauttaa asian-
        mukaisen totuusarvon.
        """
        if book_code not in self.__loans and len(self.__loans) < 3:
            self.__loans[book_code] = int(LOAN_TIME)
            return True
        else:
            return False

    def check_list(self, book_code):
        """
        Metodi tutkii, että löytyykö kirjaa lainalistasta
        ja löytäessään kirjan metodi palauttaa tunnuksen
        ja nimen emofunktion käsittelyyn.
        """
        if book_code in self.__loans:
            return self.__id, self.__holder
        else:
            return int(0), int(0)

    def return_book(self, book_code):
        """
        Metodi poistaa kirjan tunnukseen sidotusta laina-
        listasta.
        """
        self.__loans.pop(book_code)

    def info(self):
        print("Card holder:", self.__holder)
        if len(self.__loans) == 0:
            print("- No loans")
        else:
            for book in sorted(self.__loans):
                print(f"- Loan {book}, loan time left "
                      f"{self.__loans[book]} weeks")

    def go_forward(self):
        """
        Metodi päivittää tunnuksen lainakirjojen
        laina-ajat ajassa eteenpäin.
        """
        for book in self.__loans:
            if self.__loans[book] > 0:
                self.__loans[book] -= 1


def read_card_data(file_name):
    card_data = {}

    try:
        file_object = open(file_name, mode="r")

        for line in file_object:
            line = line.strip()
            strings = line.split(";")

            card_id = int(strings[0])
            card_holder = strings[1]

            new_card = Librarycard(card_id, card_holder)

            card_data[card_id] = new_card

    except OSError:
        print("Error in reading the file")
        return None

    return card_data


def read_card_id(prompt, database):
    while True:
        try:
            id = int(input(prompt))

            while id not in database:
                print("Erroneous card id, existing id's are:")
                listing(database)
                id = int(input(prompt))

            return id

        except ValueError:
            print("Erroneous card id, existing id's are:")
            listing(database)


def listing(cards):
    for card in sorted(cards):
        print(card, ":", cards[card].holder())


def borrow(library):
    """
    Funktio tarkistaa, että onko kirjaa lainattu missään vaiheessa
    ja onko kellään liikaa kirjoja lainattuna. Mikäli kaikki
    tuntuu olevan ihan hyvin funktio lisää kirjan tämän tunnuksen
    alle ja palauttaa uuden kirjaston olioista.
    """
    card = read_card_id("Card code: ", library)
    book_code = int(input("Book code: "))
    if check_for_availability(book_code, library):
        if library[card].add_to_list(book_code):
            print("Loan successful, loan time 3 weeks")
            return library
        else:
            print(f"Card {card} has already 3 loans")
            print("Loan not successful")
            return library
    return library


def remove(library):
    """
    Funktio tarkistaa, että onko kirja löytyvissä joltain ja
    poistaa kirjan tämän tunnuksista, mikäli tämä sieltä
    löytyy. Lopputuloksena palautetaan kirjasto olioista.
    """
    book_code = int(input("Book code: "))
    for id in library:
        card, name = library[id].check_list(book_code)
        card = int(card)
        if card != 0:
            break
    if card != 0:
        library[card].return_book(book_code)
        print("Book returned")
        return library
    else:
        print("This book has not been borrowed by anyone")
        return library


def pass_time(library):
    """
    Funktio käy läpi kerta kerralla jokaisen henkilön ja
    tämän omistamat kirjat ja päivittää näiden laina-ajat.
    """
    for id in library:
        library[id].go_forward()
    print("Loan times updated!")
    return library


def check_for_availability(book_code, library):
    """
    Funktio tarkistaa, että löytyykö keltään kirjaa jo
    lainattuna ja palauttaa asianmukaisen totuusarvon.
    """
    for id in library:
        card, name = library[id].check_list(book_code)
        card = int(card)
        if card != 0:
            break
    if card != 0:
        print(f"Customer {card} {name} has already borrowed "
              f"book with id {book_code}")
        return False
    else:
        return True


def main():
    library = read_card_data("library.txt")
    if library == None:
        return

    print("Welcome to Perähikiä library!")

    while True:
        command = input("Command: ")
        command = command.upper()

        if command == "I":
            card = read_card_id("Card code: ", library)
            library[card].info()

        elif command == "L":
            listing(library)

        elif command == "B":
            library = borrow(library)

        elif command == "R":
            library = remove(library)

        elif command == "W":
            library = pass_time(library)

        elif command == "" or command == "Q":
            print("Thankyou and good bye!")
            return

        else:
            print("Erroneous command!")
            print("The commands are:")
            print("Info")
            print("List librarycards")
            print("Borrow")
            print("Return")
            print("new Week")


if __name__ == "__main__":
    main()
