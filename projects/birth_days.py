from datetime import datetime


users = [
    {'name': 'Sarah Hunt', 'birthday': datetime(2016,10,20)}, 
    {'name': 'Patricia Villarreal','birthday': datetime(1993,10,25)}, 
    {'name': 'Dustin Gonzalez', 'birthday': datetime(2020,10,21)},
    {'name': 'Joy Chase', 'birthday': datetime(1979,10,15)},
    {'name': 'Morgan Hunter', 'birthday': datetime(2008,10,17)},
    {'name': 'Jeffrey Brown', 'birthday': datetime(2011,10,19)},
    {'name': 'Jeff Bro', 'birthday': datetime(2005,10,21)},
    {'name': 'Jenny Brayan', 'birthday': datetime(2001,10,17)}
    ]

def birthdays(users):

    today = datetime.today().date()

    birthday_calendar = {'Monday': [],
                        'Tuesday': [],
                        'Wednesday': [],
                        'Thursday': [],
                        'Friday': [],
                        'Saturday': [],
                        'Sunday': []}

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date() 
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            continue
        else:
            delta_days = (birthday_this_year - today).days
            if delta_days <= 7:
                day_of_week = birthday_this_year.strftime("%A")

                if day_of_week in ("Sunday","Saturday"):
                    day_of_week = 'Monday'
                    birthday_calendar[day_of_week].append(name)
                else:
                    birthday_calendar[day_of_week].append(name)

    for key, value in birthday_calendar.items():
        string = ''
        for i in range(len(value)):
            if value[-1] == value[i]:
                string += value[i]
            else:
                string += f'{value[i]}, '
        print(f'{key}: {string}')


birthdays(users)