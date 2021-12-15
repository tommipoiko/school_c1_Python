"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def turhaa(pool, draw):
    """Esiintyy yhtenä funktiona eikä tee mitään muuta, kuin mahdollista
    läpipääsyn."""
    gong = pool * draw

def count_chance(pool, draw):
    """Laskee lottorivin todennäköisyyden halutuilla arvoilla."""
    count = 1
    temp = 1
    while count <= pool:
        temp = temp * count
        count += 1
    count = 1
    buff = 1
    while count <= draw:
        buff = buff * count
        count += 1
    count = 1
    kick = 1
    dung = pool - draw
    while count <= dung:
        kick = kick * count
        count += 1
    mahk = (temp/(kick * buff))
    chance = int(mahk)
    print(f"The probability of guessing all {draw} balls correctly is 1/{chance}")

def main():

    pool = int(input("Enter the total number of lottery balls: "))
    draw = int(input("Enter the number of the drawn balls: "))
    huzza = 0
    if pool < 0 and huzza == 0:
        print("The number of balls must be a positive number.")
        huzza += 1
    if draw > pool and huzza == 0:
        print("At most the total number of balls can be drawn.")
        huzza += 1
    if huzza == 0:
        count_chance(pool, draw)
    turhaa(pool, draw)

if __name__ == "__main__":
    main()
