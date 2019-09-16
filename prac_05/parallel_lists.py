"""Program that joins two parallel lists into a single dictionary"""

names = ["Jack", "Jill", "Harry"]
dates_of_birth = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]

birthday_dict = {}

for i in range(len(names)):
    name = names[i]
    birthday_dict[name] = dates_of_birth[i]
print(names)
print(dates_of_birth)
print(birthday_dict)