import csv

filename = "students.csv"
NAME_INDEX = 1
STUDENT_NUMBER = 0

def main():
    entered_i_number = int(input("What is the I number of the student you would like to find?"))
    print("")
    student_dictionary = read_dictionary(filename=filename, key_column_index=NAME_INDEX)
    print(f"The student number you entered is {entered_i_number}. Which shows the student name of {student_dictionary[STUDENT_NUMBER]}.")
    

def read_dictionary(filename , key_column_index):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}

    with open(filename, 'rt') as file_to_read:
        student_dictionary_from_csv = csv.reader(file_to_read)
        next(student_dictionary_from_csv)
        for row_list in student_dictionary_from_csv:
            if len(row_list) != 0:
                key=row_list[key_column_index]
                dictionary[key] = row_list
    return dictionary



if __name__ == "__main__":
    main()


### Requirments #######

# Get an I-Number from the user, 
# use the I-Number to find the corresponding student name in the dictionary, 
# print the name.
# If a user enters an I-Number that doesn’t exist in the dictionary, your program must print the message, No such student.