import math
import datetime as dt
import pathlib
import os

def get_volume(tire_width, tire_aspect_ratio, tire_diameter):
    top_value_front = (math.pi)* tire_width **2 * (tire_aspect_ratio * (tire_width * tire_aspect_ratio + 2540 * tire_diameter))
    bottom_divider = top_value_front/10000000000

    return bottom_divider

def write_to_file(tire_width,tire_aspect_ratio, tire_diameter, calculated_tire_size, current_date):
    with open()

tire_width = int(input("Enter the width of the tire in mm (ex 205): "))
tire_aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
tire_diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

calculated_tire_size = get_volume(tire_width=tire_width, tire_aspect_ratio=tire_aspect_ratio, tire_diameter=tire_diameter)
print(f"The Approximate vloume is {calculated_tire_size:.2f} Liters.")

current_date = dt.datetime.now()
print(current_date)

