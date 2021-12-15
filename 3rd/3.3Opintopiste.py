"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def main():

    number = int(input("Enter the number of months: "))
    round = 1
    fail = 0
    sum = 0
    end = 0
    while round <= number:
        nop = int(input(f"Enter the number of credits in month {round}: "))
        if nop == 0:
            fail += 1
        if nop > 0:
            fail = 0
        if fail == 2:
            print("")
            print("You did have too many study breaks!")
            end = 1
            break
        sum += nop
        avg = sum / number
        round += 1
    if end == 0:
        if avg >= 5:
            print("")
            print(f"You are a full time student and your monthly credit "
                  f"point average is {avg:.1f}.")
        if avg < 5:
            print("")
            print(f"Your monthly credit point average {avg:.1f} does not "
                  f"classify you as a full time student.")


if __name__ == "__main__":
    main()
