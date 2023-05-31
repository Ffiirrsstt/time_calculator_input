def day_add(hour_more, hour_start, sum_hour, day, forcal_hour, meridiem): 
    hour_more = int(hour_more)
    hour_start = int(hour_start)
    while True:
        if hour_start == 12:
            if sum_hour//12 <2 :
                break
        if sum_hour==12:
            if meridiem == 'AM':
                break
        if hour_more<24:
            if meridiem=='AM':
                break
            day += sum_hour//24
            if forcal_hour==1:
                if hour_start != '12' and meridiem == 'PM' :
                        day +=1 
        else :
            answer = sum_hour//24
            day += answer
        break
    return day

def day_and_day_later(sum_minute, hour_more, hour_start, sum_hour, day, forcal_hour, for_cal_hour, meridiem):
    day_later = None
    if forcal_hour==1:
        if hour_start != '12':
            if meridiem == 'PM' :
                day_later = '(next day)'
    elif forcal_hour>1:
        hour_more = int(hour_more)
        if hour_more%24==0:
            if hour_more==24:
                if int(sum_minute) < 60 :
                    day_later = '(next day)'
                else :
                    day_later = for_cal_hour//24
                    if meridiem == 'PM' and hour_start== '11':
                        day_later+= 1
                    if day_later == 1 :
                        day_later = '(next day)'
                    else :
                        day_later = '({} days later)'.format(day_later)
            elif hour_more!=24:
                day_later = hour_more//24
                day_later = '({} days later)'.format(day_later)
        elif forcal_hour==2:
            day_later = '(next day)'
        elif forcal_hour%2 ==0:
            day_later = for_cal_hour//24
            day_later = '({} days later)'.format(day_later)
        else:
            day_later = 1 + (for_cal_hour//24)
            day_later = '({} days later)'.format(day_later)
    if day != '0' :
        day = day_add(hour_more, hour_start, sum_hour, day, forcal_hour, meridiem)
        if int(sum_minute) > 60 :
            if meridiem == 'PM' and hour_start== '11':
                if int(hour_more)>=24:
                    day = forcal_hour + 1
        if day>7:
            day%=7
    return day,day_later

def day_convert(day):
    day = day.lower() 
    if day == 'monday' :
        day = 1
    elif day == 'tuesday' : 
        day = 2
    elif day == 'wednesday' : 
        day = 3
    elif day == 'thursday' : 
        day = 4
    elif day == 'friday' : 
        day = 5
    elif day == 'saturday' : 
        day = 6
    elif day == 'sunday' : 
        day = 7
    elif day != '0' :
        day = False
    return day

def day_convert_back(day):
    if day == 1 :
        day = 'Monday'
    elif day == 2 : 
        day = 'Tuesday'
    elif day == 3 : 
        day = 'Wednesday'
    elif day == 4 : 
        day = 'Thursday'
    elif day == 5 : 
        day = 'Friday'
    elif day == 6 : 
        day = 'Saturday'
    elif day == 7 : 
        day = 'Sunday'
    elif day == '0' :
        day = None
    return day

def if_hour_day(sum_minute, hour_more, hour_start, meridiem, sum_hour, day, forcal_hour, for_cal_hor):
    if (sum_hour%12) == 0:
        day, day_later = day_and_day_later(sum_minute, hour_more, hour_start, sum_hour, day,forcal_hour, for_cal_hor, meridiem)
        sum_hour = 12
    else :
        day, day_later = day_and_day_later(sum_minute, hour_more, hour_start, sum_hour, day, forcal_hour, for_cal_hor, meridiem)
        sum_hour %= 12
    return sum_hour, day, day_later

def if_covert_AM_PM_for12(sum_minute, hour_more, hour_start, meridiem, sum_hour, day, forcal_hour, for_cal_hor):
    if sum_hour//12 <2 :
        sum_hour, day, day_later = if_hour_day(sum_minute, hour_more,hour_start, meridiem, sum_hour, day, forcal_hour, for_cal_hor)
    else:
        meridiem, sum_hour, day, day_later = if_covert_AM_PM(minute_more, hour_more, hour_start, meridiem, sum_hour, day, forcal_hour, for_cal_hor)
    return meridiem, sum_hour, day, day_later

def cal_more_for_AM_PM(sum_hour, minute_more, hour_more, meridiem_copy, meridiem):
    while True :
        hour_more = int(hour_more)
        if hour_more>=24:
            if hour_more%24 == 0:
                minute_more = int(minute_more)
                if minute_more!= 0:
                    if sum_hour//12==0:
                        return meridiem_copy
                        break
                return meridiem_copy
                break
            else :
                if sum_hour%24==0:
                    return meridiem_copy
        return meridiem
        break

def if_covert_AM_PM(sum_minute, minute_more, hour_more, hour_start, meridiem, sum_hour, day, forcal_hour, for_cal_hor):
    meridiem_copy = meridiem
    sum_hour_copy = sum_hour
   
    if meridiem == 'PM' :
        meridiem = 'AM'
        sum_hour, day, day_later = if_hour_day(sum_minute, hour_more, hour_start, meridiem_copy, sum_hour, day, forcal_hour, for_cal_hor)
    elif meridiem == 'AM' :
        meridiem = 'PM'
        sum_hour, day, day_later = if_hour_day(sum_minute, hour_more, hour_start, meridiem_copy, sum_hour, day, forcal_hour, for_cal_hor)
    meridiem = cal_more_for_AM_PM(sum_hour_copy, minute_more, hour_more, meridiem_copy, meridiem)
    return meridiem, sum_hour, day, day_later

def add_cal_time(hour_start, minute_start, hour_more, minute_more, day=None):
    minute_start, meridiem = minute_start.split()
    h_more = 0

    sum_minute = int(minute_start)+int(minute_more)
    if sum_minute >= 60 :
        h_more = sum_minute//60
        sum_minute %= 60
    #add zero
    if sum_minute<10:
        sum_minute = '0'+str(sum_minute)

    sum_hour = int(hour_start)+int(hour_more)+h_more

    foranswer = add_cal_time_call(hour_more, minute_more, hour_start, meridiem, sum_hour, day, sum_minute, minute_start)
    return foranswer

def AM_AM_PM_PM(meridiem):
    if meridiem=='AM':
        meridiem='PM'
    elif meridiem=='PM':
        meridiem='AM'
    return meridiem

def for_not_ch(meridiem):
    if meridiem=='AM':
        meridiem='AM'
    elif meridiem=='PM':
        meridiem='PM'
    return meridiem

def add_cal_time_call(hour_more, minute_more, hour_start, meridiem, sum_hour, day, sum_minute, minute_start):
    day_later = None
    for_cal_hor = sum_hour
    forcal_hour = sum_hour//12
    meridiem_copy = meridiem
    sum_min = int(minute_more)+int(minute_start)

    if hour_start == '12':
        if (sum_hour%12) != 0:
            meridiem, sum_hour, day, day_later = if_covert_AM_PM_for12(minute_more, hour_more, hour_start, meridiem, sum_hour, day, forcal_hour, for_cal_hor)
        day, day_later = day_and_day_later(sum_minute, hour_more, hour_start, sum_hour, day,forcal_hour, for_cal_hor, meridiem)
        sum_12 = sum_hour%12
        if sum_12 != 0 :
            sum_hour = sum_12
        else :
            sum_hour = 12
        hour_more = int(hour_more)
        if hour_more%12==0:
            if hour_more%24!=0:
                meridiem = AM_AM_PM_PM(meridiem_copy)
    elif sum_hour>=12:
        meridiem, sum_hour, day, day_later = if_covert_AM_PM(sum_min, minute_more, hour_more, hour_start, meridiem, sum_hour, day, forcal_hour, for_cal_hor)
    hour_more = int(hour_more)
    hour_more_1 = hour_more%24
    if hour_more_1==23:
        if sum_min//60 == 1:
            meridiem = AM_AM_PM_PM(meridiem_copy)
    if for_cal_hor >= 24:
        if for_cal_hor-(for_cal_hor//24*24) <= 12 :
            if hour_start != '12':
                if hour_more_1+int(hour_start) == 11:
                    if sum_min >=60 :
                        meridiem = AM_AM_PM_PM(meridiem_copy)
                    else : 
                        meridiem = for_not_ch(meridiem_copy)
                else : 
                        meridiem = for_not_ch(meridiem_copy)
        else :
            meridiem = AM_AM_PM_PM(meridiem_copy)
    format_send = '{}:{} {}'.format(sum_hour,sum_minute,meridiem)
    day = day_convert_back(day)
    if day:
        format_send = format_send+', {}'.format(day)
    if day_later:
        format_send = format_send+' {}'.format(day_later)
    return format_send

def input_day():
    while True:
        print('\nYou can select'
            , 'Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday,'
            , 'or choose not to specify a day by entering \'0\'.\n')

        print('Which day of the week do you want the start date to be?'
            , 'If you don\'t want to specify a day for calculation, please enter \'0\'.'
            , sep='\n')
        day = input(': ')
        day = day_convert(day)
        if day:
            break
    return day

def input_time_more():
    while True:
        time_more = input('Please enter the duration time you want to add in the correct format \n[e.g., 24:20] : ')
        if ':' in time_more :
            hour_more, minute_more = time_more.strip().split(':')
            return hour_more, minute_more
            
        else :
            print('\nPlease enter the duration time in the format \'24:20\' only,'
            ,'indicating the hours and minutes to be added to the start time.')

def wrong_input_start():
    print('\nPlease enter the start time in the format \'11:43 PM\' only.')
    add_time()
    
def add_time():
    time_start = input('\nPlease enter the desired start time in the correct format \n[e.g., 11:43 PM] : ').upper()
    if not 'PM' in time_start : 
        if not 'AM' in time_start : 
            wrong_input_start()
            return
    if ':' in time_start :
        hour_start, minute_start = time_start.strip().split(':')
        if not ' ' in time_start.strip():
            wrong_input_start()
            return
    else :
        wrong_input_start()
        return

    hour_more, minute_more = input_time_more()

    day = input_day()

    # output
    time = add_cal_time(hour_start.strip(), minute_start.strip(), hour_more.strip(), minute_more.strip(), day)
    print('\n'+time)

def test():
    hour_start, minute_start, hour_more, minute_more = ['11','59 pm','23','59']
    day = '0'
    print('{}:{} , {}:{}'.format(hour_start, minute_start, hour_more, minute_more))
    print(day)
    day = day_convert(day)
    minute_start = minute_start.upper()
    time = add_cal_time(hour_start.strip(), minute_start.strip(), hour_more.strip(), minute_more.strip(), day)
    print('\n'+time)

#Just check if the input and output are correct.
#It is not used for checking text filling patterns.
def loop_for_test():
    while True :
        add_time()
        y = input('\nQ : ')
        if y=='y':
            break

add_time()