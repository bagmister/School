import math
import datetime as dt
import pathlib
import os

def get_volume(tire_width, tire_aspect_ratio, tire_diameter):
    top_value_front = (math.pi)* tire_width **2 * (tire_aspect_ratio * (tire_width * tire_aspect_ratio + 2540 * tire_diameter))
    bottom_divider = top_value_front/10000000000

    return bottom_divider

def write_to_file(tire_width, tire_aspect_ratio, tire_diameter, calculated_tire_size, current_date):
    file_path = pathlib.PureWindowsPath('C:/Users/Bagmister.DESKTOP-8VDDAPO/Dev/School/CES111/Week2/volumes.txt')
    with open('file_path', "a") as file:
        calculated_tire_values_to_write_to_file = [f"{tire_width} \n",f"{tire_aspect_ratio} \n", f"{tire_diameter} \n", f"{calculated_tire_size} \n", f"{current_date} \n"]
        file.writelines(calculated_tire_values_to_write_to_file)

tire_width = int(input("Enter the width of the tire in mm (ex 205): "))
tire_aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
tire_diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

calculated_tire_size = get_volume(tire_width=tire_width, tire_aspect_ratio=tire_aspect_ratio, tire_diameter=tire_diameter)
print(f"The Approximate vloume is {calculated_tire_size:.2f} Liters.")

current_date = dt.datetime.now()
print(current_date)
write_contents = write_to_file(tire_width, tire_aspect_ratio, tire_diameter, calculated_tire_size, current_date)