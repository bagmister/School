import csv
import pathlib
import os
from datetime import datetime


# Things that my program needs to do:
# Print the store name at the top of the receipt. - done
# Print the list of ordered items.
# Sum and print the number of ordered items.
# Sum and print the subtotal due.
# Compute and print the sales tax amount. Use 6% as the sales tax rate.
# Compute and print the total amount due.
# Print a thank you message. - done
# Get the current date and time from your computer’s operating system and print the current date and time. - done
# Include a try block and except blocks to handle FileNotFoundError, PermissionError, and KeyError.


ITEM_INDEX = 0
PRICE_INDEX = 3
QUANTITY_OF_ITEM = 1
UNIQUE_ITEM_CODE_INDEX = 0
tax_rate_given = .06

store_name = "SMITHS"
current_date_and_time = datetime.now()
thank_you_message = "Thanks for shopping at Smiths."


def main():
    key_column_index = 0
#     must doe the following to meet business requirments:
#     Calls the read_dictionary function and stores the compound dictionary in a variable named products_dict.
    path_to_files = pathlib.PureWindowsPath(r'C:\Users\Bagmister.DESKTOP-8VDDAPO\Dev\School\CES111\Week10')
    products_csv_file_name = "products.csv"
    try:
        products_file_path_with_name = os.path.join(path_to_files, products_csv_file_name)
    except:
        print("file not found. Re-define where the file is to be found. Don't foget the file path to update.")
    products_dictionary = read_dictionary(file_to_read=products_file_path_with_name, key_column_index=key_column_index)
    print(products_dictionary)
    
    requests_csv_file_name = "request.csv"
    requests_file_path_with_name = os.path.join(path_to_files, requests_csv_file_name)
    requests_order= read_order_in_csv_format(file_to_read=requests_file_path_with_name, reference_dictionary=products_dictionary)
    convert_reqest_to_dictionary = convert_list_to_dictionary(list_to_convert=requests_order)

    print(convert_reqest_to_dictionary)
    customer_subtotal = 0
    calculated_sales_tax = calculate_tax(tax_rate=tax_rate_given, subtotal=customer_subtotal)
    total_with_sales_tax = calculate_sales_tax_total(tax_amount=calculated_sales_tax, subtotal=customer_subtotal)
    total_items_sold = calculate_total_items_sold(requests_order)
    structure_recipt_to_print(store_name=store_name, time=current_date_and_time, item_list=requests_order, subtotal=customer_subtotal, tax_amount=calculated_sales_tax, total_with_sales_tax=total_with_sales_tax, thank_you_message=thank_you_message, number_of_tiems_sold=total_items_sold)
    
# def convert_list_to_dictionary(list_to_convert):
#     refined_list = []
#     for row in list_to_convert:

def calculate_total_items_sold(requests_order):
    print("")

def read_order_in_csv_format(file_to_read, reference_dictionary):
    order_in_list_format = []
    new_dict_revised_order = {UNIQUE_ITEM_CODE_INDEX:QUANTITY_OF_ITEM}
    with open(file_to_read, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                item_code = row_list[UNIQUE_ITEM_CODE_INDEX]
                quntity= row_list[QUANTITY_OF_ITEM]
                item_code_and_quanity = [item_code, int(quntity)]
                for item in reference_dictionary:
                    if item_code == item:
                        row_list[1] += quntity
                        item_code_and_quanity = [item_code, int(quntity)]
                    new_dict_revised_order.update({item_code_and_quanity[0]:item_code_and_quanity[1]})
                order_in_list_format += item_code_and_quanity
            print(item_code_and_quanity)

    return unique_order_in_list_format

def calculate_sales_tax_total(subtotal, tax_amount):
    tax_with_total = subtotal + tax_amount
    return tax_with_total

def calculate_tax(subtotal, tax_rate):
    tax_amount = subtotal * tax_rate
    return tax_amount


def structure_recipt_to_print(store_name, time, item_list, subtotal, tax_amount, total_with_sales_tax, thank_you_message, number_of_tiems_sold):
    print(store_name)
    print(f"{time:%A %I:%M %p}")
    print("")
    print(item_list)
    print("")
    print(f"Number of items sold: {number_of_tiems_sold}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax_amount:.2f}")
    print(f"Total: ${total_with_sales_tax:.2f}")
    print(thank_you_message)
# def filter_dictionary_for_order(item_to_find, order_list, reference_list, List_to_search_though):
#     for item in order:

#         price = row_list[PRICE_INDEX]
#     return ordered_list

# def print_list_or_ordered_items(order):
#     for item in order:
#         print(item)

#     return order_by_line

# Prints the products_dict.
# Opens the request.csv file for reading.
# Skips the first line of the request.csv file because the first line contains column headings.
# Uses a loop that reads and processes each row from the request.csv file. Within the body of the loop, your program must do the following for each row:
# Use the requested product number to find the corresponding item in the products_dict.

def read_dictionary(file_to_read, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
        
    print(f"File I am reading from is {file_to_read}. If this is not intentional please correct this error.")
    dictionary = {}
    with open(file_to_read, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list
    return dictionary

if __name__ == "__main__":
    main()