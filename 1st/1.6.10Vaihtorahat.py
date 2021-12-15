"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""

def main():
    pass

    hinta=input("Purchase price: ")
    maksu = input("Paid amount of money: ")
    price=int(hinta)
    paid = int(maksu)
    if price == 0:
        print("No change")
    elif paid-price < 1:
        print("No change")
    else:
        print("Offer change:")
        vec1=paid-price
        vec2=vec1//10
        if vec2 > 0:
            print(vec2, "ten-euro notes")
        vec3=vec1-vec2*10
        vec4=vec3//5
        if vec4 > 0:
            print(vec4, "five-euro notes")
        vec5=vec3-vec4*5
        vec6=vec5//2
        if vec6 > 0:
            print(vec6, "two-euro coins")
        vec7=vec5-vec6*2
        vec8=vec7//1
        if vec8 > 0:
            print(vec8, "one-euro coins")

if __name__ == "__main__":
    main()