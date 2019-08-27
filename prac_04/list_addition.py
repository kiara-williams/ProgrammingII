def main():
    list_one = [1, 2, 3]
    list_two = [4, 5, 6]
    summed_values = []
    for value in list_one:
        add_value = list_two[list_one.index(value)]
        new_value = value + add_value
        summed_values.append(new_value)
    print(list_one,"+", list_two,"=", summed_values)


main()