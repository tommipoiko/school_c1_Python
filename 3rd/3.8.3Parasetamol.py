"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def calculate_dose(weight, time, tot):
    """Laskee sallitun annosmäärän tarvitsijalle sopivilla muuttujilla."""
    max6 = int(weight * 15)
    max24 = 4000
    if time < 6:
        return 0
    if time >= 6 and (max6 + tot) <= max24:
        return max6
    else:
        return max24 - tot


def main():
    weight = int(input("Patient's weight (kg): "))
    time = int(input("How much time has passed from the previous dose (full "
                     "hours): "))
    tot = int(input("The total dose for the last 24 hours (mg): "))
    calculate_dose(weight, time, tot)
    print(f"The amount of Parasetamol to give to the patient: {calculate_dose(weight, time, tot)}")

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)


if __name__ == "__main__":
  main()
