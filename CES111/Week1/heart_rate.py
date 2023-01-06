time = 220

def get_target_heart_rate(age, time):
    print(f"Calculating maximum heart rate based on {age} give.")
    maximum_target_rate = time - age
    return maximum_target_rate

def get_heart_rate_65_range(maximum_target_rate):
    heart_rate_65 = (maximum_target_rate *.65)
    return heart_rate_65

def get_heart_rate_85_range(maximum_target_rate):
    heart_rate_85 = (maximum_target_rate *.85)
    return heart_rate_85

print("When you physically exercise to strengthen your heart, you should maintain your heart rate within a range for at least 20 minutes. To find that range")
print("")
print("")
age = input("What is your age?: ")

persons_max_heart_rate = get_target_heart_rate(age)
persons_heart_rate_65_range = get_heart_rate_65_range(persons_max_heart_rate)
persons_heart_rate_85_range = get_heart_rate_85_range(persons_max_heart_rate)

print(f"Your heart simply will not beat faster than this maximum {persons_max_heart_rate}.")
print(f"When exercising to strengthen your heart, you should keep your heart rate between 65% {persons_heart_rate_65_range} and 85% {persons_heart_rate_85_range} of your heart’s maximum rate {persons_max_heart_rate}.")



"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""