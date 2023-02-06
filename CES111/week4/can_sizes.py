import math

# Your program must compute the volume of all 12 can sizes.
# Your program must compute the surface area of all 12 can sizes.
# Your program must compute and print the storage efficiency of all 12 can sizes.

def main():
    
    name_can_1 = "#1 Picnic" 
    radius_can_1 = 6.83
    height_can_1 = 10.16

    name_can_2 = "#1 Tall" 
    radius_can_2 = 7.78
    height_can_2 = 11.91
    cost_can_2 = 0.43
    cost_can_1 = 0.28
    name_can_3 = "#2" 
    radius_can_3 = 8.73
    height_can_3 = 11.59
    cost_can_3 = 0.45
    name_can_4 = "#2.5" 
    radius_can_4 = 10.32
    height_can_4 = 11.91
    cost_can_4 = 0.61
    name_can_5 = "#3 Cylinder" 
    radius_can_5 = 10.79
    height_can_5 = 17.78
    cost_can_5 = 0.86
    name_can_6 = "#5" 
    radius_can_6 = 13.02
    height_can_6 = 14.29
    cost_can_6 = 0.83
    name_can_7 = "#6Z" 
    radius_can_7 = 5.40
    height_can_7 = 8.89
    cost_can_7 = 0.22
    name_can_8 = "#8Z short" 
    radius_can_8 = 6.83
    height_can_8 = 7.62
    cost_can_8 = 0.26
    name_can_9 = "#10" 
    radius_can_9 = 15.72
    height_can_9 = 17.78
    cost_can_9 = 1.53
    name_can_10 = "#211" 
    radius_can_10 = 6.83
    height_can_10 = 12.38
    cost_can_10 = 0.34
    name_can_11 = "#300" 
    radius_can_11 = 7.62
    height_can_11 = 11.27
    cost_can_11 = 0.38
    name_can_12 = "#303" 
    radius_can_12 = 8.10
    height_can_12 = 11.11
    cost_can_12 = 0.42

    compute_whole(radius=radius_can_1, height=height_can_1, name=name_can_1)
    compute_whole(radius=radius_can_2, height=height_can_2, name=name_can_2)
    compute_whole(radius=radius_can_3, height=height_can_3, name=name_can_3)
    compute_whole(radius=radius_can_4, height=height_can_4, name=name_can_4)
    compute_whole(radius=radius_can_5, height=height_can_5, name=name_can_5)
    compute_whole(radius=radius_can_6, height=height_can_6, name=name_can_6)
    compute_whole(radius=radius_can_7, height=height_can_7, name=name_can_7)
    compute_whole(radius=radius_can_8, height=height_can_8, name=name_can_8)
    compute_whole(radius=radius_can_9, height=height_can_9, name=name_can_9)
    compute_whole(radius=radius_can_10, height=height_can_10, name=name_can_10)
    compute_whole(radius=radius_can_11, height=height_can_11, name=name_can_11)
    compute_whole(radius=radius_can_12, height=height_can_12, name=name_can_12)

def compute_whole(radius, height, name):
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficency(volume, surface_area)
    print(f"{name} {storage_efficiency:.2f}")

def compute_storage_efficency(volume, surface_area):
    storage_efficency =  volume / surface_area
    return storage_efficency

def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2*math.pi*radius * (radius + height)
    return surface_area


main()




