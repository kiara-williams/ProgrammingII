from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0
    current_taxi = None
    print("Let's drive!")
    menu_selection = get_menu_choice()
    while menu_selection != 'q':
        if menu_selection == 'c':
            for taxi in taxis:
                print(taxi)
            while current_taxi is None:
                try:
                    taxi_selection = int(input("Choose taxi:"))
                except ValueError:
                    print("You need to enter a number")
                    taxi_selection = int(input("Choose taxi:"))
                except IndexError:
                    print("That taxi is not in the list")
                    taxi_selection = int(input("Choose taxi:"))
                current_taxi = taxis[taxi_selection]
        else:
            # finish

        print(bill)
        menu_selection = get_menu_choice()


def get_menu_choice():
    print(MENU)
    user_input = input(">>>").lower()
    while user_input != "q" and user_input != "c" and user_input != "d":
        print("Invalid menu option")
        print(MENU)
        user_input = input(">>>").lower()
    return user_input
