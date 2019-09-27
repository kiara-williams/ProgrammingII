from prac_08.silver_service_taxi import SilverServiceTaxi

my_hummer = SilverServiceTaxi("Hummer", 200, 4)
print(my_hummer)
my_taxi = SilverServiceTaxi("Silver Service Taxi 1", 100, 2)
my_taxi.drive(18)
print("Current fare for {} is ${:.2f}".format(my_taxi.name, my_taxi.get_fare()))