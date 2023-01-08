import math


def get_volume(tire_width, tire_aspect_ratio, tire_diameter):
    top_value_front = (math.pi)* tire_width **2 * (tire_aspect_ratio * (tire_width * tire_aspect_ratio + 2540 * tire_diameter))
    bottom_divider = top_value_front/10000000000

    return bottom_divider

tire_width = int(input("Enter the width of the tire in mm (ex 205): "))
tire_aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
tire_diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

calculated_tire_size = get_volume(tire_width=tire_width, tire_aspect_ratio=tire_aspect_ratio, tire_diameter=tire_diameter)
print(f"The Approximate vloume is {calculated_tire_size:.2f} Liters.")

a = 1
b = 3
c = -2
result = a + b * 7 % 4 - c

print(result)