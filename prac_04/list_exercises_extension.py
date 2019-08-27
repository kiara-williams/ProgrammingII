"""Program that takes in x numbers and prints some interesting facts"""

def main():
    print("Enter as many numbers as you like. Enter a negative number when finished")
    number_list = []
    number_count = 0
    new_number = int(input("Number 1: "))
    if new_number >= 0:
        number_list.append(new_number)
        number_count += 1
    while new_number >= 0:
        """infinite loop with negative number exit condition"""
        new_number = int(input("Number {}: ".format(number_count + 1)))
        if new_number >= 0:
            """check that number is not exit number before adding to list for stats"""
            number_list.append(new_number)
            number_count += 1
    if not number_list:
        """check for empty list"""
        print("No numbers were entered")
    else:
        list_average = sum(number_list) / number_count
        print("The first number is {}".format(number_list[0]))
        print("The last number is {}".format(number_list[-1]))
        print("The smallest number is {}".format(min(number_list)))
        print("The largest number is {}".format(max(number_list)))
        print("The average of these numbers is {:.1f}".format(list_average))


main()