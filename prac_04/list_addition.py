def main():
    list_one = [1, 2, 3]
    list_two = [4, 5, 6]
    summed_values = []
    if len(list_one) == len(list_two):
        for value in list_one:
            add_value = list_two[list_one.index(value)]
            new_value = value + add_value
            summed_values.append(new_value)
    elif len(list_one) > len(list_two):
        for value in list_one:
            try:
                add_value = list_two[list_one.index(value)]
                new_value = value + add_value
                summed_values.append(new_value)
            except IndexError:
                summed_values.append(value)
    else:
        for value in list_one:
            add_value = list_two[list_one.index(value)]
            new_value = value + add_value
            summed_values.append(new_value)
        missed_values = list_two[value:]
        summed_values += missed_values
    print(list_one,"+", list_two,"=", summed_values)


main()