item_count = int(input("Enter the number of items"))
if item_count <= 0:
    print("You need to enter at least one item")
item_total = 0
item_prices = []
for i in range(item_count):
    item = float(input("Enter the item's price"))
    item_total += item
    item_prices.append(item)
print("Number of items: " + str(item_count))
for i in item_prices:
    print("Price of item: $ {:.2f}".format(i))
if item_total > 100:
    item_total = item_total - (item_total * 0.1)
    print("Total price for {} items/s is ${:.2f}".format(item_count, item_total))
else:
    print("Total price for {} item/s is ${:.2f}".format(item_count, item_total))
    

"""Program to continously enter item prices if unknown number of items, with option to summarise when finished entering.

item = float(input("Enter the first item's price"))
if item <= 0:
    print("You need to enter the price of at least one item")
    item = float(input("Enter the first item's price"))
item_total = 0
item_count = 0
item_prices = []
while item > 0:
    item_total += item
    item_prices.append(item)
    item_count += 1
    item = float(input("Enter the next price, or enter 0 if finished"))
print("Number of items: " + str(item_count))
for i in item_prices:
    print("Price of item: $ {:.2f}".format(i))
if item_total > 100:
    item_total = item_total - (item_total * 0.1)
    print("Total price for {} items/s is ${:.2f}".format(item_count, item_total))
else:
    print("Total price for {} item/s is ${:.2f}".format(item_count, item_total))
