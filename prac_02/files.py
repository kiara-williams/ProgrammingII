FILE = "name.txt"
NUMBER_FILE = "numbers.txt"

# asks for input and prints name to file

read_file = open(FILE, "w")

name = str(input("Please enter your name: "))
print(name, file=read_file)

read_file.close()

# reads name from file and prints it to console.

write_file = open(FILE, "r")

name = write_file.readline()
stripped_name = name.strip()
print("Your name is", stripped_name)

write_file.close()

# reads number file and adds contents. Currently using file w/ 17 and 42, but scalable for larger files.

read_file = open(NUMBER_FILE, "r")
file_list = read_file.readlines()
total = 0

for line in file_list:
    line = line.strip()
    total += int(line)
print("The total is", total)
