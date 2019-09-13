"""CP1404 Practical - Car Simulator Exercise"""

from prac_06.car import Car

MENU = """Menu:
d) drive
r) refuel
q) quit"""


def main():
    car_name = input("Enter your car name: ")
    my_car = Car(100, car_name)
    menu_choice = get_menu_choice()
    while menu_choice != "q":
        if menu_choice == "d":
            distance = int(input("How many km do you wish to drive? "))
            while not validate_input(distance, "Distance"):
                distance = int(input("How many km do you wish to drive? "))
            my_car.drive(distance)
            menu_choice = get_menu_choice()
        elif menu_choice == "r":
            #refuel
            menu_choice = get_menu_choice()
        else:
            print("Invalid choice")
            print(MENU)
            menu_choice = get_menu_choice()


def get_menu_choice():
    print(MENU)
    menu_choice = input("Enter your choice: ").lower()
    return menu_choice


def  validate_input(input, type):
    if input < 0:
        print("{} must be >= 0".format(type))
        return False
    else:
        return True

main()