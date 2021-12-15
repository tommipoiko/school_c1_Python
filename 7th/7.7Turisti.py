"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    print("Dictionary contents:")
    wordlist = ""
    for word in sorted(english_spanish):
        wordlist += word + " "
    printlist = wordlist.rstrip()
    printlist = printlist.replace(" ", ", ")
    print(printlist)

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":
            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish[word]}")
            else:
                print("The word", word,
                      "could not be found from the dictionary.")

        elif command == "A":
            eng = input("Give the word to be added in English: ")
            engword = eng.strip()
            span = input("Give the word to be added in Spanish: ")
            spanword = span.strip()
            english_spanish[engword] = spanword
            print("Dictionary contents:")
            wordlist = ""
            for word in sorted(english_spanish):
                wordlist += word + " "
            printlist = wordlist.rstrip()
            printlist = printlist.replace(" ", ", ")
            print(printlist)

        elif command == "R":
            delete = input("Give the word to be removed: ")
            remove = delete.strip()
            if remove in english_spanish:
                del english_spanish[remove]
            else:
                print("The word", word,
                      "could not be found from the dictionary.")

        elif command == "P":
            print("")
            print("English-Spanish")
            for word in sorted(english_spanish):
                print(f"{word} {english_spanish[word]}")
            print("")
            print("Spanish-English")
            spanish_english = dict()
            for word in english_spanish:
                spanish_english[english_spanish[word]] = word
            for word in sorted(spanish_english):
                print(f"{word} {spanish_english[word]}")
            print("")

        elif command == "T":
            sent = input("Enter the text to be translated into Spanish: ")
            words = sent.split()
            rnd = 0
            product = ""
            while rnd < len(words):
                if words[rnd] in english_spanish:
                    product += english_spanish[words[rnd]] + " "
                else:
                    product += words[rnd] + " "
                rnd += 1
            print("The text, translated by the dictionary:")
            print(product.rstrip())

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


if __name__ == "__main__":
    main()
