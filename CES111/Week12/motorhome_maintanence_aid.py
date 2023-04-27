import tkinter
import tkinter.ttk
import csv
import pandas as pd
from datetime import datetime
import dateutil
import motorhome_maintanence_config as m_config


# To do. Get user input for millage. Most calculations will be bassed off this value

welcome_message = "Greetings! I am here to assist you with keeping track of your Motorhome maintanence."
def main(welcome_message):
    print(welcome_message)
    current_millage = float(input("To get started please enter your current Odometer reading for the main engine. : "))
    current_date = datetime.today().strftime('%m/%Y')
    print(f"Current month and year are: {current_date}.")
    replaced_all_tires_age = calculate_age_of_tire(current_date=current_date, tire_install_date=m_config.all_tires_combined_bought_new_install_date)
    print(f"Date all tires where repelaced: {replaced_all_tires_age} ago.")
    program_start(current_millage=current_millage, current_date=current_date)

def tire_maintanenece(current_millage, current_date):
    tire_maintananece_selector = int(input("What would you like to enter for tires? Enter 1 for New Tires. 2 for Tire rotation. 3 for selecting individual tires replaced.:  "))
    if tire_maintananece_selector == 1:
        try:
            replace_tires = tire_replacment()
        except Exception as e:
            print(f"EFFOR unable to update replacing all tires. {e}")
        return replace_tires

    if tire_maintananece_selector == 2:
        try:
            tire_rotation_date_value = tire_rotation()
            return tire_rotation_date_value
        except Exception as e:
            print(f"ERROR updating tire rotation. {e}")
        return
    if tire_maintananece_selector == 3:
        tire_to_update_number = int(input("Which Tire was replaced?: Enter a number from 1 to 8 for the tire you want to edit, with order of tires being. 1 - driver front, 2 - passenger front, 3 - drive axle outer driver tire, 4 - drive axle inner driver tire, 5 - drive axle passnager outer tire, 6 - drive axle inner passanger tire, 7 - tag axle driver side - if equipped, 8 - tag axle passanger side - if equipped.:  "))
        date_of_replacment = input("What date was this tire installed?")
        try:
            update_single_tire = single_tire_update(tire_to_update_number, date_of_replacment)
        except Exception as e:
            print(f"ERROR updating replacment tire : {e}")
            exit()
        return update_single_tire

def calculate_age_of_tire(current_date , tire_install_date):
    converted_curent_date = datetime.strptime(current_date, '%m/%Y').date()
    converted_install_date = datetime.strptime(tire_install_date, '%m/%Y').date()
    current_age_of_tires = str(converted_curent_date - converted_install_date)
    return current_age_of_tires

def tire_replacment():
    all_tires_year = input("What year was the year all tires where replaced?: enter in format YYYY")
    all_tires_month = input("What Month where the tires purchased in? Enter in the format MM meaning include the 0 in front of single digits.: ")
    all_tires_combined = f"{all_tires_month}/{all_tires_year}"
    return all_tires_combined

def tire_rotation():
    tire_rotation_date = input("Enter the month and year the tire rotation was done in the format MM/YYYY : ")
    confirm_tire_rotation_date = bool(f"You entered {tire_rotation_date}. Is this correct? y for yes and n for no.")
    if confirm_tire_rotation_date == True:
        tire_maintannce_choice = False
        return tire_rotation_date
    if tire_maintannce_choice == False:
        print(f"You entered {tire_rotation_date}. Let's get the correct date.")
        return

def single_tire_update(tire_to_update_number, date_of_replacment):
    match tire_to_update_number:
        case 1:
            m_config.individual_tire_dictionary.update({'driver_front': date_of_replacment})
            print("updated driver_front")
        case 2:
            m_config.individual_tire_dictionary.update({'passanger_front': date_of_replacment})
            print("updated passanger_front")
        case 3:
            m_config.individual_tire_dictionary.update({'drive_axle_outer_driver': date_of_replacment})
            print("updated drive_axle_outer_driver")
        case 4:
            m_config.individual_tire_dictionary.update({'drive_axle_inner_driver': date_of_replacment})
            print("updated drive_axle_inner_driver")
        case 5:
            m_config.individual_tire_dictionary.update({'drive_axle_outer_passanger': date_of_replacment})
            print("updated drive_axle_outer_passanger")
        case 6:
            m_config.individual_tire_dictionary.update({'drive_axle_inner_passanger': date_of_replacment})
            print("updated drive_axle_inner_passanger")
        case 7:
            m_config.individual_tire_dictionary.update({'tag_axle_driver': date_of_replacment})
            print("updated tag_axle_driver")
        case 8:
            m_config.individual_tire_dictionary.update({'tag_axle_passanger': date_of_replacment})
            print("updated tag_axle_passanger")
    edit_another_tire = bool("Is there another tire you would like to enter? Y for yes or N for no.")
    print(m_config.individual_tire_dictionary)
    return

def calculate_next_year_to_change_oil_by(day_of_oil_change):
    if day_of_oil_change == None:
        day_of_oil_change = datetime.today()
    oil_change_date_for_next_year = day_of_oil_change + dateutil.relativedelta(years=1)
    return oil_change_date_for_next_year

def get_next_oil_change_millage(last_oil_change, current_millage):
    if last_oil_change == .0 or None:
        print("No recoreded last oil change date. Using current millage to base next oil change on.")
        next_oil_change = current_millage + 3000
    else:  
        print(f"Last recorded date for an oil change is: {last_oil_change}")
        next_oil_change = last_oil_change + 3000
    return next_oil_change

def update_oil_change(current_millage, current_date, day_of_oil_change):
    if day_of_oil_change == None or 0.0:
        print("Oil change was not done today. let's update...")
        most_recent_oil_change = m_config.oil_changes_dictionary.get('most_recent_oil_change')
        next_oil_Change_millage = get_next_oil_change_millage(last_oil_change=most_recent_oil_change,  current_millage=current_millage)
        print("Updating milage to when next oil change needs to be done around.")
        m_config.oil_changes_dictionary.update({'next_oil_change_millage': next_oil_Change_millage})
        next_year_oil_cahnge_date = calculate_next_year_to_change_oil_by(day_of_oil_change)
        print("Updating date to replace oil by should millage not be reached.")
        m_config.oil_changes_dictionary.update({'replace_oil_by_if_milage_is_not_met_in_a_year': next_year_oil_cahnge_date})
    elif day_of_oil_change == current_date:
        print("Oil change was not done today. let's update...")
        m_config.oil_changes_dictionary.update({'most_recent_oil_change': float(current_millage)})
        print("Updating milage to when next oil change needs to be done around.")
        m_config.oil_changes_dictionary.update({'next_oil_change_millage': float(current_millage)})
        next_year_oil_cahnge_date = calculate_next_year_to_change_oil_by(day_of_oil_change)
        print("Updating date to replace oil by should millage not be reached.")
        m_config.oil_changes_dictionary.update({'replace_oil_by_if_milage_is_not_met_in_a_year': next_year_oil_cahnge_date})
    return
    
def calculate_next_year_to_change_trans_fluid_by(day_of_trans_change):
    if day_of_trans_change == None:
        day_of_trans_change = datetime.today().strftime('%m/%Y')
    day_of_oil_change_converted = datetime.date(day_of_trans_change)
    years_to_add = day_of_oil_change_converted.year + 2
    oil_change_date_for_next_year = day_of_oil_change_converted.replace(year=years_to_add).strftime('%m-%YYYY')
    return oil_change_date_for_next_year

def update_transmission_fluid_change(current_millage, current_date, day_of_trans_change):
    print("Updating transmission values....")
    next_trans_fluid_Change_millage = get_next_oil_change_millage(m_config.oil_changes_dictionary.get(["most_recent_trans_fluid_change"]))
    if day_of_trans_change == None:
        print("Oil change was not done today. let's update...")
        m_config.trans_fluid_changes_dictionary.get("most_recent_trans_fluid_change")
        print("Updating milage to when next oil change needs to be done around.")
        m_config.trans_fluid_changes_dictionary.update({'next_trans_fluid_change_millage', float(next_trans_fluid_Change_millage)})
        next_year_oil_cahnge_date = calculate_next_year_to_change_oil_by(day_of_trans_change)
        print("Updating date to replace oil by should millage not be reached.")
        m_config.trans_fluid_changes_dictionary.update({'replace_trans_fluid_by_if_milage_is_not_met_in_a_year', next_year_oil_cahnge_date})
    elif day_of_trans_change == current_date:
        print("Oil change was not done today. let's update...")
        m_config.trans_fluid_changes_dictionary.update({'most_recent_trans_fluid_change', float(current_millage)})
        print("Updating milage to when next oil change needs to be done around.")
        m_config.trans_fluid_changes_dictionary.update({'next_trans_fluid_change_millage', float(current_millage)})
        next_year_oil_cahnge_date = calculate_next_year_to_change_oil_by(day_of_trans_change)
        print("Updating date to replace oil by should millage not be reached.")
        m_config.oil_changes_dictionary.update({'replace_trans_fluid_by_if_milage_is_not_met_in_a_year', next_year_oil_cahnge_date})
    return

def chassis_maintanenece(current_millage, current_date):
    chassis_selection = int(input("What kind of maintanence are you entering? enter 1 for engine oil change. 2 for transmission fluid change. 3 for other engine related maintanence items. 4 for lubrication and grease points. 5 for axles and differentials. 6 for braking system. 7 for heater and AC. 8 for electrical systems:  "))
    if chassis_selection == 1:
        print("You selected engine oil change.")
        recent_oil_change_date = input("Was the oil change done today? y for yes n for no.: ")
        if recent_oil_change_date.lower() == "y":
            print("Updating records to show as trans fluid change done today.")
            update_oil_change_value = update_oil_change(current_millage, current_date, day_of_oil_change=None)
        elif recent_oil_change_date.lower() == "n":
            day_of_oil_change = input("What day was the oil change perfomred on? Enter in format of mm/dd/yyyy: ")
            update_oil_change_value = update_oil_change(current_millage, current_date, day_of_oil_change=day_of_oil_change)
    elif chassis_selection == 2:
        print("You selected Transmission Fluid change.")
        recent_trans_fluid_change_date = bool(input("Was the trans fluid change done today? y for yes n for no.: "))
        if recent_trans_fluid_change_date == True:
            print("Updating records to show as oil change done today.")
            update_trans_fluid_change_value = update_transmission_fluid_change(current_millage, current_date, day_of_trans_change=None)
        elif recent_trans_fluid_change_date == False:
            day_of_tans_fluid_change = input("What day was the oil change perfomred on? Enter in format of mm/dd/yyyy: ")
            update_trans_fluid_change_value = update_transmission_fluid_change(current_millage, current_date, day_of_trans_change=day_of_tans_fluid_change)
    elif chassis_selection == 3:
        print("You selected general engine bay maintanenece.")
    elif chassis_selection == 4:
        print("You selected lube and grease.")
    elif chassis_selection == 5:
        print("You selected axle and differntial.")
    elif chassis_selection == 6:
        print("You selected brakes system")
    elif chassis_selection == 7:
        print("You selected AC/heater(main engine ran) systems")
    elif chassis_selection == 8:
        print("You selected electrical(main engine ran) systems")

def house_maintanence(current_millage, current_date):
    print("Starting House section... ")

def program_start(current_millage, current_date):
    program_entrance = input("What kind of maintannece would you like to find out next to do or update? Enter 'tires' for tire related. Enter chassis for the chassis and this includes drivetrain. Enter house for living area: ")
    if program_entrance.lower() == "tires":
        print(f"Entered: {program_entrance}. Starting tires section... ")
        tires = tire_maintanenece(current_millage, current_date)
    elif program_entrance.lower() == "chassis":
        print(f"Entered: {program_entrance}. Starting chassis section... ")
        chassis = chassis_maintanenece(current_millage, current_date)
    elif program_entrance.lower() == "house":
        print(f"Entered: {program_entrance}. Starting house(living area box) section... ")
        chassis = house_maintanence(current_millage, current_date)
    else:
        print(f"{program_entrance} is not a valid option. Would you like to enter maintanence?")
        continue_with_maintanence_entered = input("Enter 'y' for yes and 'n' for no: ")
        return continue_with_maintanence_entered    

main(welcome_message)