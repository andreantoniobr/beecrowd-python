def get_hours(hour_start, hour_end):
    if hour_end > hour_start:
        hours = hour_end - hour_start    
    else:
        hours = (24 - hour_start) + hour_end
    return hours

def get_minutes(minute_start, minute_end):
    if minute_end >= minute_start:
        minutes = minute_end - minute_start    
    else:
        minutes = (60 - minute_start) + minute_end
    return minutes

def get_elapsed_time(hour_start, hour_end, minute_start, minute_end):
    hours = get_hours(hour_start, hour_end)
    minutes = get_minutes(minute_start, minute_end)

    if hour_end == hour_start and minute_end > minute_start:
        hours = 0
        
    if minute_end < minute_start:
        hours -= 1

    return hours, minutes

def main():
    data = input().split()
    hour_start = int(data[0])
    minute_start = int(data[1])
    hour_end = int(data[2]) 
    minute_end = int(data[3])
    hours, minutes = get_elapsed_time(hour_start, hour_end, minute_start, minute_end)
    print(f"O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)")

main()