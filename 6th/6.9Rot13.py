"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    word = text.lower()
    if word in regular_chars:
        if word == text:
            index = regular_chars.index(word)
            return encrypted_chars[index]
        elif word != text:
            index = regular_chars.index(word)
            return encrypted_chars[index].upper()
    else:
        return text


def row_encryption(text):
    """
        Encrypts its parameter using ROT13 encryption technology.

        :param text: str,  string to be encrypted
        :return: str, <text> parameter encrypted using ROT13
        """

    rnd = 0
    complete = ""
    while rnd < len(text):
        complete += encrypt(text[rnd])
        rnd += 1
    return complete


def main():
    words = row_encryption(str(input("")))
    print(words)


if __name__ == "__main__":
    main()
