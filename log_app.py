from datetime import datetime, timedelta
from zoneinfo import *
import time
import os.path


def month_to_name(num):
    if num == 1:
        return 'January'
    if num == 2:
        return 'February'
    if num == 3:
        return 'March'
    if num == 4:
        return 'April'
    if num == 5:
        return 'May'
    if num == 6:
        return 'June'
    if num == 7:
        return 'July'
    if num == 8:
        return 'August'
    if num == 9:
        return 'September'
    if num == 10:
        return 'October'
    if num == 11:
        return 'November'
    if num == 12:
        return 'December'



zone = ZoneInfo("US/Central")
dt = datetime.now(tz=zone)

message = str(input('Enter a note for your entry (press Enter to leave this part blank): '))

if message != '':
    message = ' - {0}'.format(message)

entry = month_to_name(dt.month) + ' ' + str(dt.day)+ ', ' + str(dt.year) + message + '\n'

if os.path.isfile('./mylog.txt'):
    mode = 'a'
else:
    mode = 'w'

f = open('mylog.txt', mode, encoding='utf-8')
f.writelines(entry)
f.close()

