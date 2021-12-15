"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def main():
    numberof = dict()
    print("Enter rows of text for word counting. Empty row to quit.")
    sentence = input("")
    sentence = sentence.lower()
    sentence_list = sentence.split()
    while sentence != "":
        sentence = input("")
        sentence = sentence.lower()
        sentence_list += sentence.split()
    for number in sentence_list:
        numberof[number] = 0
    for number in sentence_list:
        numberof[number] += 1
    for yikes in sorted(numberof):
        print(f"{yikes} : {numberof[yikes]} times")


if __name__ == "__main__":
    main()
