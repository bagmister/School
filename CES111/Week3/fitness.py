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
    bmi = body_mass_index(weight=killograms_weight, height=height_in_centimeters)
    pass

def compute_age(birth_str):
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1
    print(f"Based on what you entered your age is {years}.")
    return years

def kg_from_lb(pounds):
    lb_in_kg= pounds * .45359237
    
    print(f"Your weight in Killograms is: {lb_in_kg}")
    return lb_in_kg

def cm_from_in(inches):
    converted_inch_to_cent = inches * 2.54 
    
    print(f"Your hight in Centemeters is {converted_inch_to_cent}. Based on the number in inches you provided.")
    return converted_inch_to_cent

def body_mass_index(weight, height):
    bmi = 10000 * weight / height **2
    print(f"Your Body Mass Index is {bmi:.2f} based on your height and weight entered.")
    return bmi

def basal_metabolic_rate(gender, weight, height, age):
    if gender == 'f':
        bmr = 447.593 + (9.247 *weight) + (3.098 * height) - (4.330 * age)
    else:
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    print(f"Your Basal Metabolic Rate based on you being a {gender} (f for female and m for male) is {bmr:.2f}.")

    return

main()