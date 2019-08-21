"""Program for converting temperature"""

def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            temperature = float(input("Celsius: "))
            new_temperature = calculate_fahrenheit(temperature)
            print("Result: {:.2f} F".format(new_temperature))
        elif choice == "F":
            temperature = float(input("Fahrenheit: "))
            new_temperature = calculate_celsius(temperature)
            print("Result: {:.2f} C".format(new_temperature))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def calculate_celsius(temperature):
    """Convert fahrenheit to celsius"""
    new_temperature = 5 / 9 * (temperature - 32)
    return new_temperature


def calculate_fahrenheit(temperature):
    """Convert celsius to fahrenheit"""
    new_temperature = temperature * 9.0 / 5 + 32
    return new_temperature


main()