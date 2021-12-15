"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def longest_substring_in_order(text):
    """Etsii aakkoshommia juu, vaikeaa on näemmä."""
    rnd = 1
    length = len(text)
    if length > 0:
        seq = text[0]
        des = seq
    while rnd < length:
        if length > 1:
            if text[rnd] > text[rnd-1]:
                seq += text[rnd]
            else:
                seq = text[rnd]
            if len(des) < len(seq):
                des = seq
            rnd += 1
    if text.isalpha():
        return des
    else:
        return ""


def main():
    des = longest_substring_in_order(str(input()))
    print(des)


if __name__ == "__main__":
    main()
