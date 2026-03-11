from datetime import time, datetime

def to_usual_time_format(hour=0, minute=0, meridiem=None):
    errors=str()
    if (minute >=60 or minute<0) or (hour >11 or hour<0) or (meridiem!='am' and meridiem!='pm'):
        if minute >=60 or minute<0:
            errors = str(minute)+' '
        if hour >11 or hour<0:
            errors+= str(hour)+' '
        if meridiem!='am' and meridiem!='pm':
            errors+= str(meridiem)+' '
        return f'Некорректный ввод: {errors}'
    if meridiem=='pm':
        hour+=12
    if hour<10:
       hour='0'+str(hour)
    if minute<10:
        minute='0'+str(minute)
    time_new=str(hour)+':'+str(minute)
    time_onj=datetime.strptime(time_new,'%H:%M')
    time_onj=datetime.time(time_onj)
    return time_onj
        

print(to_usual_time_format(0, 0, 'am'))  # 00:00:00
print(to_usual_time_format(0, 0, 'pm'))  # 12:00:00
print(to_usual_time_format(11, 30, 'pm'))  # 23:30:00
print(to_usual_time_format(5, 45, 'am'))  # 05:45:00