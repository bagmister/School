import math

def calculate_number_of_boxes(number_of_items, number_of_items_per_box):
    total_amount = math.ceil(number_of_items / number_of_items_per_box)
    print(f"For {number_of_items} items, packing {number_of_items_per_box} items in each box, you will need {total_amount} boxes.")
    return total_amount


number_of_items = int(input("Enter the number of items?: "))
number_of_items_per_box = int(input("Enter the number of items per box?: "))
calculated_shipping = calculate_number_of_boxes(number_of_items, number_of_items_per_box)
