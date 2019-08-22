"""Program that asks for x quick picks and generates that many random number sequences"""

import random

LOWER = 1
UPPER = 45
COUNT = 6

def main():
    num_of_picks = int(input("How many quick picks?"))
    for i in range(num_of_picks):
        used = []
        current_pick = []
        pick_format = ""
        for i in range(COUNT):
            number = random.randint(LOWER,UPPER)
            while number in used:
                number = random.randint(LOWER,UPPER)
            used.append(number)
            current_pick.append(number)
        current_pick.sort()
        for num in current_pick:
            pick_format += str(num) + " "
        print(pick_format)

main()