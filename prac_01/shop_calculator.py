item_count = int(input("Enter the number of items"))
if item_count <= 0:
    print("You need to enter at least one item")
item_total = 0
print("Number of items: " + str(item_count))
for i in range(item_count):
    item_price = float(input("Price of item {}: $".format(i + 1)))
    item_total += item_price
if item_total > 100:
    item_total = item_total - (item_total * 0.1)
print("Total price for {} item/s is ${:.2f}".format(item_count, item_total))