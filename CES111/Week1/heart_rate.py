def get_target_heart_rate(age, time):
    print(f"Calculating maximum heart rate based on {age} given.")
    maximum_target_rate = time - age
    return maximum_target_rate

def get_heart_rate_65_range(maximum_target_rate):
    heart_rate_65 = round((maximum_target_rate *.65))
    return heart_rate_65

def get_heart_rate_85_range(maximum_target_rate):
    heart_rate_85 = round((maximum_target_rate *.85))
    return heart_rate_85

print("When you physically exercise to strengthen your heart, you should maintain your heart rate within a range for at least 20 minutes. To find that range")

age = int(input("What is your age?: "))
time = 220

persons_max_heart_rate = get_target_heart_rate(age, time)
persons_heart_rate_65_range = get_heart_rate_65_range(persons_max_heart_rate)
persons_heart_rate_85_range = get_heart_rate_85_range(persons_max_heart_rate)

print(f"Your heart simply will not beat faster than this maximum {persons_max_heart_rate} bpm.")
print(f"When exercising to strengthen your heart, you should keep your heart rate between 65% {persons_heart_rate_65_range} bpm and 85% {persons_heart_rate_85_range} bpm of your heart’s maximum rate {persons_max_heart_rate} bpm.")



"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""