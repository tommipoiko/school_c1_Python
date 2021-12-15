"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def paiva_maara(day):
    """Funktio kerää listan lämpötiloista muuttujanaan annettu määrä päiviä.
    FUnktio palauttaa arvonaan kyseisen listan."""
    rnd = 1
    temp_list = []
    while rnd <= day:
        temp_list.append(float(input(f"Enter day {rnd}. temperature in Celcius: ")))
        rnd += 1
    return temp_list


def temp_laskuri(temp_list):
    """Tämä funktio laskee mediaanin ja keskiarvon muuttujana annetuista
    lämpötiloista. Funktio palauttaa arvoinaan mediaanin ja keskiarvon."""
    rnd = 0
    sum = 0
    n = len(temp_list)
    order = sorted(temp_list)
    while rnd < n:
        sum += temp_list[rnd]
        rnd += 1
    mean = sum / n
    if n % 2 == 1:
        median = order[n//2]
    else:
        median1 = order[n//2]
        median2 = order[n//2-1]
        median = (median1+median2)/2
    print()
    print(f"Temperature mean: {mean:.1f}C")
    print(f"Temperature median: {median:.1f}C")
    return mean, median


def temp_over(temp_list, mean, median):
    """Katsoo muuttujien perusteella, että mitkä lämpötilat olivat mediaanin
    yläpuolella ja tulostaa ne listaan. Ei palauta mitään arvoja."""
    print()
    rnd = 1
    print("Over or at median were:")
    while rnd <= len(temp_list):
        seq = temp_list[rnd - 1]
        if temp_list[rnd-1] >= median:
            print(f"Day {rnd:>2}. {seq:>5.1f}C difference to mean: {(seq-mean):>5.1f}C")
        rnd += 1


def temp_under(temp_list, mean, median):
    """Katsoo muuttujien perusteella, että mitkä lämpötilat olivat mediaanin
    alapuolella ja tulostaa ne listaan. Ei palauta mitään arvoja."""
    print()
    rnd = 1
    print("Under median were:")
    while rnd <= len(temp_list):
        seq = temp_list[rnd - 1]
        if temp_list[rnd - 1] < median:
            print(f"Day {rnd:>2}. {seq:>5.1f}C difference to mean: {(seq - mean):>5.1f}C")
        rnd += 1


def main():
    temp_list = paiva_maara(int(input("Enter amount of days: ")))

    (mean, median) = temp_laskuri(temp_list)

    temp_over(temp_list, mean, median)

    temp_under(temp_list, mean, median)


if __name__ == "__main__":
    main()
