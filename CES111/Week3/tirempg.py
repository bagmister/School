
def miles_per_gallon(start_od, ending_od, gallons_used):
    mpg = (ending_od - start_od) /  gallons_used
    print(f"The cacluated milage based on the numbers provided is {mpg:.1f} mpg per gallon.")
    return mpg

def lp100k_from_mpg(mpg_calculated):
    lp100k = 235.215 / mpg_calculated
    return lp100k

def main():
    start_od = float(input("What is the starting odometer reeding in miles?: "))
    ending_od = float(input("What is the ending odometer reading in miles?: "))
    gallons_used = float(input("How many gallons where used?: "))
    
     
    mpg_calculated = miles_per_gallon(start_od, ending_od, gallons_used)
    mpg_calculated_per_100k  = lp100k_from_mpg(mpg_calculated)
    print(f"mpg_calculated_per_100k is {mpg_calculated_per_100k:.2f}")

main()