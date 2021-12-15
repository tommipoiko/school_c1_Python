"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def main():
    pass

    pelaaja1=input("Player 1, enter your choice (R/P/S): ")
    pelaaja2=input("Player 2, enter your choice (R/P/S): ")
    player1=str(pelaaja1)
    player2=str(pelaaja2)
    if player1 == "R" and player2 == "P":
        print("Player 2 won!")
    elif player1 == "S" and player2 == "P":
        print("Player 1 won!")
    elif player1 == "P" and player2 == "P":
        print("It's a tie!")
    elif player1 == "R" and player2 == "R":
        print("It's a tie!")
    elif player1 == "S" and player2 == "R":
        print("Player 2 won!")
    elif player1 == "P" and player2 == "R":
        print("Player 1 won!")
    elif player1 == "R" and player2 == "S":
        print("Player 1 won!")
    elif player1 == "S" and player2 == "S":
        print("It's a tie!")
    else:
        print("Player 2 won!")

if __name__ == "__main__":
    main()
