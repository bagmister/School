


# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("What is your Gender? Enter m for Male and f for Female: ").lower()
    birth_str = input("What is your birthdate? Enter in the following format YYYY-MM-DD: ") 
    weight  = float(input("What is your weight?: "))
    height = float(input("What is your height in inches?: "))
    age = compute_age(birth_str)
    killograms_weight = kg_from_lb(weight)
    height_in_centimeters = cm_from_in(height)
    bmr = basal_metabolic_rate(age=age,gender=gender, weight=killograms_weight, height=height_in_centimeters) # must calcluate different for M and F
    bmi = body_mass_index(weight=killograms_weight, height=height_in_centimeters, age=age, gender=gender)

    # Print the results for the user to see.
    pass


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    lb_in_kg= pounds * .45359237
    return lb_in_kg


def cm_from_in(inches):
    converted_inch_to_cent = inches * 2.54 
    return converted_inch_to_cent


def body_mass_index(weight, height, gender, age):

    if gender == 'f':
        bmr = 447.593 + 9.247 weight + 3.098 height - 4.330 age
    else:
        bmr = 88.362 + 13.397 weight + 4.799 height - 5.677 age

    return bmr


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    return




# Call the main function so that
# this program will start executing.

