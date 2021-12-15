"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    name = "a"
    nimi = name.strip()
    while nimi != "":
        name = input("Enter product name: ")
        nimi = name.strip()
        if nimi in PRICES:
            print(f"The price of {nimi} is {PRICES[nimi]:.2f} e")
        elif nimi not in PRICES and nimi != "":
            print(f"Error: {nimi} is unknown.")
    print("Bye!")


if __name__ == "__main__":
    main()
