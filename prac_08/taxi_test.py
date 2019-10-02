from prac_08.taxi import Taxi

my_car = Taxi("Prius 1", 100)
my_car.drive(40)
print(my_car)
print("Current fare is ${:.2f}".format(my_car.get_fare()))
my_car.start_fare()
my_car.drive(100)
print(my_car)
print("Current fare is ${:.2f}".format(my_car.get_fare()))