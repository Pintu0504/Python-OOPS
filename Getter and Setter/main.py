from item import Item

item1 = Item("MyItem", 500, 2)

# Set the name of Item => Setter
# item1.price = 400

# Get the name of Item => Getter
item1.apply_discount()
print(item1.calculate_total_price())