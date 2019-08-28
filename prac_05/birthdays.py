NUM_PEOPLE = 5

def main():
    ages = {}
    for i in range(NUM_PEOPLE):
        name = input("Enter person {}'s name: ".format(i + 1))
        birthdate = input("Enter {}'s birthdate using dd/mm/yyyy: ".format(name))
        day, month, year = birthdate.split("/")
        if int(month) >= 9:
            person_age = 2018 - int(year)
            ages[name] = person_age
        else:
            person_age = 2019 - int(year)
            ages[name] = person_age
    for name in ages:
        print(name, ages[name])


main()
