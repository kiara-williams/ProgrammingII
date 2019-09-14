"""CP1404 Practical - Car Simulator Exercise"""

from prac_06.car import Car

MENU = """Menu:
d) drive
r) refuel
q) quit"""


def main():
    car_name = input("Enter your car name: ")
    my_car = Car(100, car_name)
    menu_choice = get_menu_choice(my_car)
    while menu_choice != "q":
        if menu_choice == "d":
            distance = int(input("How many km do you wish to drive? "))
            while not validate_input(distance, "Distance"):
                distance = int(input("How many km do you wish to drive? "))
            if my_car.fuel < distance:
                print("The car drove {}km and ran out of fuel".format(my_car.fuel))
                my_car.drive(my_car.fuel)
            else:
                my_car.drive(distance)
                if my_car.fuel == 0:
                    refuel_needed = " and ran out of fuel."
                else:
                    refuel_needed = ""
                print("The car drove {}km{}".format(distance, refuel_needed))
            menu_choice = get_menu_choice(my_car)
        elif menu_choice == "r":
            refuel = int(input("How many units of fuel do you want to add to the car? "))
            while not validate_input(refuel, "Fuel amount"):
                refuel = int(input("How many units of fuel do you want to add to the car?"))
            my_car.add_fuel(refuel)
            print("Added {} units of fuel".format(refuel))
            menu_choice = get_menu_choice(my_car)
        else:
            print("Invalid choice")
            print(MENU)
            menu_choice = get_menu_choice(my_car)


def get_menu_choice(car):
    """Display car stats and menu, return user menu choice"""
    print("\n{}, fuel={}, odo={}".format(car.name, car.fuel, car.odometer))
    print(MENU)
    menu_choice = input("Enter your choice: ").lower()
    return menu_choice


def validate_input(input_string, format_string):
    """Take user input and confirm that it is a valid number"""
    if input_string < 0:
        print("{} must be >= 0".format(format_string))
        return False
    else:
        return True


main()
