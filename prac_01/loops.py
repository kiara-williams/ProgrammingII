for i in range(1, 21, 2):
    print(i, end=' ')
print() #<-- Inserts blank line

for i in range(0,101,10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

stars = int(input("Enter the number of stars you would like"))
while stars < 1:
    stars = int(input("Enter a valid number of stars"))
for i in range(stars):
    print("*", end='')
print()

num_stars = int(input("Enter the number of stars you would like"))
star_print = ""
while num_stars < 1:
    num_stars = int(input("Enter a valid number of stars"))
for i in range(num_stars):
    star_print = star_print + "*"
    print(star_print)
print()

sales = float(input("Enter sales: $"))
while sales > 0:
    if sales >= 1000:
        print("Commission: ${:.2f}".format(sales*0.15))
    else:
        print("Commission: ${:.2f}".format(sales*0.10))
    sales = float(input("Enter sales: $"))
print()
