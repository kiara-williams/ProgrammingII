"""Program that takes lists and adds the values together. Accommodates lists of different lengths"""

def main():
    list_one = [1, 2, 3, 4]
    list_two = [4, 5, 6]
    summed_values = []
    if len(list_one) == len(list_two):
        """Adds lists of the same length"""
        for value in list_one:
            new_value = add_values(list_one, list_two, value)
            summed_values.append(new_value)
    elif len(list_one) > len(list_two):
        """Adds lists if list one is longer"""
        for value in list_one:
            try:
                new_value = add_values(list_one, list_two, value)
                summed_values.append(new_value)
            except IndexError:
                """Catches last values"""
                summed_values.append(value)
    else:
        """Adds lists if list two is longer"""
        for value in list_one:
            new_value = add_values(list_one, list_two, value)
            summed_values.append(new_value)
        """Catches last values"""
        missed_values = list_two[value:]
        summed_values += missed_values
    print(list_one,"+", list_two,"=", summed_values)


def add_values(list_one, list_two, value):
    add_value = list_two[list_one.index(value)]
    new_value = value + add_value
    return new_value


main()