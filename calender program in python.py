import datetime
#ask the user to input details of birth
year=input("please enter year of birth(format yyyy): \n")
month=input("please enter month of birth(format mm): \n")
date=input("please enter day of birth(format dd): \n")
birthday=datetime.date(int(year), int(month), int(date))
print(birthday)
week_day = ['Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday']

sf = "If you were born on %s, you were born on a %s"
print(sf % (birthday, week_day[datetime.date.weekday(birthday)]))
print("Martin thanks you for using this program press any button to exit")
input()




