import csv

key_column_index = 0

def main():
#     must doe the following to meet business requirments:
#     Calls the read_dictionary function and stores the compound dictionary in a variable named products_dict.
# Prints the products_dict.
# Opens the request.csv file for reading.
# Skips the first line of the request.csv file because the first line contains column headings.
# Uses a loop that reads and processes each row from the request.csv file. Within the body of the loop, your program must do the following for each row:
# Use the requested product number to find the corresponding item in the products_dict.
    print()


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
        
    print(f"File I am reading from is {file_to_read}.csv. If this is not intentional please correct this error.")
    dictionary = {}
    with open(file_to_read, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list
    return dictionary