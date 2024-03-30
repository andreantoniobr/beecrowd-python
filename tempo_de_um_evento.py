def get_data():
    day = int(input().split()[1])
    hour, minute, second = map(int, input().split(" : "))
    return day, hour, minute, second

def get_days_amount(day_start, day_end):
    days = 0    
    if day_end > day_start:
        days = day_end - day_start   
    return days

def get_hours_amount(hour_start, hour_end):
    hours = 0
    if hour_end > hour_start:
        hours = hour_end - hour_start
    elif hour_end < hour_start:
        hours = (24 - hour_start) + hour_end        
    return hours

def get_minutes_amount(minute_start, minute_end): 
    minutes = 0   
    if minute_end > minute_start:
        minutes = minute_end - minute_start
    elif minute_end < minute_start:
        minutes = (60 - minute_start) + minute_end        
    return minutes

def get_seconds_amount(second_start, second_end):
    seconds = 0
    if second_end > second_start:
        seconds = second_end - second_start    
    elif second_end < second_start:
        seconds = (60 - second_start) + second_end
    return seconds

def convert_days_to_seconds(days):    
    return days * 24 * 60 * 60

def convert_hours_to_seconds(hours):    
    return hours * 60 * 60

def convert_minutes_to_seconds(minutes):    
    return minutes * 60

def get_event_time(seconds):
    days = seconds // (24 * 60 * 60)
    seconds %= (24 * 60 * 60) 
    hours = seconds // (60 * 60)
    seconds %= (60 * 60) 
    minutes = seconds // (60)
    seconds %= 60
    return days, hours, minutes, seconds

def print_event_time(days, hours, minutes, seconds):
    print(f"{days} dia(s)")
    print(f"{hours} hora(s)")
    print(f"{minutes} minuto(s)")
    print(f"{seconds} segundo(s)")

def main():
    day_start, hour_start, minute_start, second_start = get_data()
    day_end, hour_end, minute_end, second_end = get_data()
    
    days_amount = get_days_amount(day_start, day_end)
    hours_amount = get_hours_amount(hour_start, hour_end)
    minutes_amount = get_minutes_amount(minute_start, minute_end)
    seconds_amount = get_seconds_amount(second_start, second_end)    
    
    if second_end < second_start:
        minutes_amount -= 1
    if minute_end < minute_start:
        hours_amount -= 1   
    if hour_end < hour_start:
        days_amount -= 1  
          
    days_to_seconds = convert_days_to_seconds(days_amount)
    hours_to_seconds = convert_hours_to_seconds(hours_amount)
    minutes_to_seconds = convert_minutes_to_seconds(minutes_amount)    
    
    event_time_seconds = days_to_seconds + hours_to_seconds + minutes_to_seconds + seconds_amount
    days, hours, minutes, seconds = get_event_time(event_time_seconds)
    print_event_time(days, hours, minutes, seconds)

main()