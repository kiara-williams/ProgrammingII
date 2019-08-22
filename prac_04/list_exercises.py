"""Program that takes in x numbers and prints some interesting facts"""

NUMBER_RANGE = 5

def main():
    print("Enter {} numbers".format(NUMBER_RANGE))
    number_list = []
    for i in range(NUMBER_RANGE):
        new_number = int(input("Number: "))
        number_list.append(new_number)
    list_average = sum(number_list)/NUMBER_RANGE
    print("The first number is {}".format(number_list[0]))
    print("The last number is {}".format(number_list[-1]))
    print("The smallest number is {}".format(min(number_list)))
    print("The largest number is {}".format(max(number_list)))
    print("The average of these numbers is {:.1f}".format(list_average))


main()