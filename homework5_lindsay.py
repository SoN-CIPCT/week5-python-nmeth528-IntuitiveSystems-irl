# Week 5 Assignment: Lists and Tuples

# ============ LIST EXERCISE ============

# Create a list that contains 6 items
my_list = ["apple", "banana", "cherry", "date", "elderberry", "fig"]

# Print the items in the list to the output console
print("Items in the list:", my_list)

# Print the first two items using a slice
first_two = my_list[0:2]
print(f"The first two items in the list are: {first_two[0]}, {first_two[1]}")

# Print the middle two items using a slice
middle_two = my_list[2:4]
print(f"The middle two items in the list are: {middle_two[0]}, {middle_two[1]}")

# Print the first and last items using indexes
first_item = my_list[0]
last_item = my_list[-1]
print(f"The first and last items in the list are: {first_item}, {last_item}")


# ============ TUPLE EXERCISE ============

# A restaurant only offers five basic foods on its menu
menu = ("burger", "pizza", "salad", "pasta", "tacos")

# Print each item on the menu using a for loop
print("\nOriginal Menu:")
for item in menu:
    print(item)

# The restaurant has updated its menu, replacing two of the items
# Copy the tuple replacing two of the foods on the menu
updated_menu = ("burger", "sushi", "salad", "ramen", "tacos")

# Print each item on the revised menu using a loop
print("\nRevised Menu:")
for item in updated_menu:
    print(item)
