"""CP1404 Practical - Guitar function testing"""

from prac_06.guitar import Guitar

def main():
    first_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    second_guitar = Guitar("Ibanez RG8", 2013, 509.15)

    first_guitar_age = first_guitar.get_age()
    first_guitar_vintage = first_guitar.is_vintage()
    second_guitar_age = second_guitar.get_age()
    second_guitar_vintage = second_guitar.is_vintage()

    print("{} get_age() - Expected 97. Got {}".format(first_guitar.name, first_guitar_age))
    print("{} get_age() - Expected 6. Got {}".format(second_guitar.name, second_guitar_age))
    print("{} is_vintage() - Expected True. Got {}".format(first_guitar.name, first_guitar_vintage))
    print("{} is_vintage() - Expected False. Got {}".format(second_guitar.name, second_guitar_vintage))

main()
