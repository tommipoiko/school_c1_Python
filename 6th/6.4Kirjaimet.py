"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def main():
    text = input("Enter a word: ")
    vowel = 0
    consonant = 0
    for letter in text:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "y":
            vowel += 1
        else:
            consonant += 1
    print(f"The word \"{text}\" contains {vowel} vowels and {consonant} consonants.")


if __name__ == "__main__":
    main()
