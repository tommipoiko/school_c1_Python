"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def reverse_name(nimi):
    """Jalla jalla hahaha moi mitä kuuluu."""
    nimet2 = nimi.strip()
    nimet11 = nimet2.split(",")
    if len(nimet11) == 2:
        if nimet11[0] == "" and nimet11[1] == "":
            uusinimi2 = ""
        elif nimet11[0] == "" or nimet11[1] == "":
            nimet01 = nimet11[0].strip()
            nimet02 = nimet11[1].strip()
            nimet03=[nimet01,nimet02]
            uusinimi2 = "".join(nimet03)
        else:
            nimet111 = nimet11[0]
            nimet112 = nimet11[1]
            nimet211 = nimet111.strip()
            nimet212 = nimet112.strip()
            nimet = [nimet211, nimet212]
            uusinimi = nimet[1]," ",nimet[0]
            uusinimi2 ="".join(uusinimi)
    elif len(nimet11)==1:
        nimet3 = nimi.strip(",")
        nimet4 = nimet3
        nimet5 ="".join(nimet4)
        nimet6 =nimet5.strip()
        uusinimi2=nimet5
    else:
        nimi1=nimi.strip()
        uusinimi2=nimi

    return uusinimi2


def main():
    print(reverse_name(","))


if __name__ == "__main__":
    main()
