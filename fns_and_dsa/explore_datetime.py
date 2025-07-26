from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    year = current_date.year
    month = f"{current_date.month :02}"
    day = f"{current_date.day:02}"
    hour = f"{current_date.hour:02}"
    minutes = f"{current_date.minute:02}"
    second = f"{current_date.second:02}"
    print(f"{year}-{month}-{day} {hour}:{minutes}:{second}") # “YYYY-MM-DD HH:MM:SS”.
    return current_date


def calculate_future_date():
    user_input = input("Enter the number of days to add to the current date: ")
    days_to_add = int(user_input) 
    today_date = datetime.now()
    duration_to_add = timedelta(days=days_to_add)
    future_date = today_date + duration_to_add
    year = future_date.year
    month = f"{future_date.month :02}"
    day = f"{future_date.day :02}"
    print(f"{year}-{month}-{day}") # “YYYY-MM-DD”.
        
   
