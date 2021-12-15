"""
COMP.CS.100
Tommi Poikolainen
050093232
"""

tuki=input("Enter the amount of the study benefits: ")
benefits=float(tuki)
korko=1.0117
index=float(korko)
result=benefits*index
print("If the index raise is 1.17 percent, the study benefit,")
print("after a raise, would be", result, "euros")
print("and if there was another index raise, the study")
result2=result*index
print("benefits would be as much as", result2 , "euros")