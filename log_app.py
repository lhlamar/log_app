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
        self.time = dt.time
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
            if 'lucas' in message_lower:
                if os.path.isfile('./mylog.txt'):
                    mode = 'a'
                else:
                    mode = 'w'
                f = open('mylog.txt', mode, encoding='utf-8')
                f.writelines('Hey aiden, if you\'re seeing this that means you typed my name as\n'
                             + 'one of your entries, which I\'ll assume means you\'re thinking\n'
                             + 'about me for one reason or another. I wanted to let you know\n'
                             + 'that I really care about you and miss you so much and haven\'t\n'
                             + 'really gone a day '
                             + 'without thinking about you. I really hope you\'re doing well\n'
                             + 'but then there\'s another selfish part of me that hopes you\n'
                             + 'aren\'t just because I\'m not and I don\'t want you to be doing\n'
                             + 'well without me. I know that\'s super selfish and dumb but it\'s true\n'
                             + 'which is so annoying. I was really missing you a lot today and wanted\n'
                             + 'to text you so bad and let you know that I was thinking about you\n'
                             + 'but I didn\'t because I know that you need space to get over me\n'
                             + 'so I\'m doing this instead. I miss you so much though. I miss\n'
                             + 'your smile, I miss your laugh, I miss your annoying little bites, I\n'
                             + 'miss how freaking pretty you are. I hate how much I like your new\n'
                             + 'haircut because it is not making this easier for me lol but it\n'
                             + 'does look really good on you. I hope everything is going well with\n'
                             + 'school and the raptor center and all that. I also really hope you\n'
                             + 'don\'t move on from me to fast as I will likely not move too soon myself.\n'
                             + 'I know that\'s also selfish of me but it would really hurt me.\n'
                             + 'I know Sean and Mel broke up so a piece of me is worried that you\n'
                             + 'and Sean are gonna rebound with each other if you haven\'t already.\n'
                             + 'Anyways, if you do end up seeing this, some reassurance about that\n'
                             + 'would be really nice to hear from you. Anyways, just know I care\n'
                             + 'about you and I love you. That\'s all I think.\n')
                f.close()
        return message

    def write_entry(self):
        entry = (self.month_to_name(self.month) + ' ' + str(self.day)+ ', ' + str(self.year) + self.message
        + str(self.time)  +'\n')
        if os.path.isfile('./mylog.txt'):
            mode = 'a'
        else:
            mode = 'w'
        f = open('mylog.txt', mode, encoding='utf-8')
        f.writelines(entry)
        f.close()

my_log = Log()
my_log.write_entry()


