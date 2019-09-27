from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    menu_selection = get_menu_choice()
    while menu_selection != 'q':
        if menu_selection == 'c':
            # finish
        if menu_selection == 'd':
            #finish
        get_menu_choice()


def get_menu_choice():
    print(MENU)
    user_input = input(">>>").lower()
    while user_input != "q" and user_input != "c" and user_input != "d":
        print("Invalid menu option")
        print(MENU)
        user_input = input(">>>").lower()
    return user_input
