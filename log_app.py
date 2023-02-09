from datetime import datetime, timedelta
from zoneinfo import *
import time
import os.path

class Log():
    def __init__(self):
        dt = datetime.now(tz=ZoneInfo("US/Central"))
        self.year = dt.year
        self.day = dt.day
        self.month = dt.month
        self.message= self.prompt()
    def month_to_name(self, num):
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
    def prompt(self):
        self.message = str(input('Enter a note for your entry (press Enter to leave this part blank): '))
        if self.message != '':
            self.message = ' - {0}'.format(self.message)
    def write_entry(self):
        entry = self.month_to_name(my_log.month) + ' ' + str(self.day)+ ', ' + str(self.year) + self.message + '\n'
        if os.path.isfile('./mylog.txt'):
            mode = 'a'
        else:
            mode = 'w'
        f = open('mylog.txt', mode, encoding='utf-8')
        f.writelines(entry)
        f.close()

my_log = Log()
my_log.write_entry()


