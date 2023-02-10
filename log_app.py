from datetime import datetime, timedelta
from zoneinfo import *
import time
import csv
import os.path

class Log():
    def __init__(self):
        dt = datetime.now(tz=ZoneInfo("US/Central"))
        self.year = dt.year
        self.day = dt.day
        self.month = dt.month
        self.hour = dt.hour
        self.minute = dt.minute
        self.second = dt.second
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
        message = str(input('Enter a note for your entry (press Enter to leave this part blank): '))
        if message != '':
            message = ' - {0}'.format(message)
            message_lower=message.lower()
            if 'bird' in message_lower:
                if os.path.isfile('./mylog.txt'):
                    mode = 'a'
                else:
                    mode = 'w'
                f = open('mylog.txt', mode, encoding='utf-8')
                f.writelines('looks like you wrote the word \'bird\'! freaking bird person XD.')
                f.close()
        return message

    def write_entry(self):

        
        if not os.path.isfile('./mylog.csv'):
            with open("mylog.csv", 'w') as f:
                writer = csv.writer(f)
                writer.writerow(["Month", "Day", "Year", "Hour", "Minute", "Memo"])




        if os.path.isfile('./mylog.csv'):
            mode = 'a'
        else:
            mode = 'w'
        with open("mylog.csv", mode) as f:
            writer = csv.writer(f)
            writer.writerow([self.month_to_name(self.month), self.day, self.year, self.hour,
                             self.minute, self.message])

my_log = Log()
my_log.write_entry()


