def add_time(start_time, duration_time, starting_day_of_the_week=None):
    weekday = {'Monday': 0, 'Tuesday':1, 'Wednesday':2, 'Thursday':3, 'Friday':4, 'Saturday': 5, 'Sunday': 6}

    [start_H_M,  start_AMPM] = start_time.split(' ')
    [start_H, start_M] = start_H_M.split(':')
    start_H, start_M = int(start_H), int(start_M)

    if start_AMPM == "PM":
        start_H += 12

    [dura_H, dura_M] = duration_time.split(':')
    dura_H, dura_M = int(dura_H), int(dura_M)

    total_H = start_H + dura_H
    total_M = start_M + dura_M

    total_H += total_M//60
    total_D = total_H//24
    total_H = total_H%24
    total_M = total_M%60

    if total_H > 12:
        AMPM = 'PM'
        total_H -= 12
    
    elif total_H == 12:
        AMPM = 'PM'
    elif total_H ==0:
        total_H = 12
    else:
        AMPM = 'AM'
        
    if total_D == 0:
        n_day_after = ''
    elif total_D == 1:
        n_day_after = '(next day)'
    else:
        n_day_after = f'({ total_D } days later)'

    if starting_day_of_the_week:
        starting_day_of_the_week = starting_day_of_the_week.capitalize()
        curr_weekday = weekday.get(starting_day_of_the_week)
        total_weekday = (curr_weekday + total_D)%7
        asc_total_weekday = ', ' + list(weekday.keys())[list(weekday.values()).index(total_weekday)]
    else:
        asc_total_weekday = ''
    
    return f'{total_H}:{total_M:02} {AMPM}{asc_total_weekday} {n_day_after}'



if __name__ =="__main__":
    # print(add_time("11:06 PM", "2:02"))
    # print(add_time("3:30 PM", "2:12"))
    # print(add_time("11:59 PM", "24:05", "Wednesday"))
    print(add_time("8:16 PM", "466:02", "tuesday"))
    # print(add_time("11:55 AM", "3:12"), '----')
    
