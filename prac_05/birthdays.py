"""Program that takes names and birthdates as input and returns current age"""

NUM_PEOPLE = 5

def main():
    ages = {}
    longest_name = 0
    for i in range(NUM_PEOPLE):
        name = input("Enter person {}'s name: ".format(i + 1))
        if len(name) > longest_name:
            longest_name = len(name)
        birthdate = input("Enter {}'s birthdate using dd/mm/yyyy: ".format(name))
        day, month, year = birthdate.split("/")
        if int(month) >= 9:
            person_age = calculate_age(2018, int(year))
            ages[name] = person_age
        else:
            person_age = calculate_age(2019, int(year))
            ages[name] = person_age
    for name in ages:
        print("{:<{}} : {}".format(name, longest_name, ages[name]))

def calculate_age(current_year, birth_year):
    """Calculate age given birth year and current year"""
    person_age = current_year - birth_year
    return person_age


main()
