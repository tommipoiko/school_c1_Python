"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""


def main():
    pass

    num=int(input("How many Fibonacci numbers do you want? "))
    round=1
    sum1 = 0
    sum2 = 1
    if num == 0:
        print("1. 0")
    while round<=num-1:
        if num == 1:
            print("1. 1")
            round += 1
        else:
            if round == 1:
                print("1. 1")
            sum3 = sum1 + sum2
            print(f"{round+1}.", sum3)
            round += 1
            sum1 = sum2
            sum2 = sum3

if __name__ == "__main__":
    main()