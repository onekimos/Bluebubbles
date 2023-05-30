import random

def get_day_of_week():
    return random.choice(["Mon", "Tue", "Wed"])

def days_in_week():
    return ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def day_output(day_list):
    for day in day_list:
        if day == "Wed":
            return get_day_of_week()
        else:
             return day_list

days = days_in_week()
print(day_output(days))
