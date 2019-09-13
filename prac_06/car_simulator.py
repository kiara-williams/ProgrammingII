"""CP1404 Practical - Car Simulator Exercise"""

from prac_06.car import Car

MENU = """Menu:
d) drive
r) refuel
q) quit"""


def main():
    car_name = input("Enter your car name: ")
    my_car = Car(100, car_name)
    print(my_car)

main()