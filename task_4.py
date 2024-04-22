import datetime

def get_upcoming_birthdays(users):
    today = datetime.date.today()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)
        days_until_birthday = (birthday - today).days

        if (today + datetime.timedelta(days=days_until_birthday)).weekday() >= 5:
            days_until_birthday += 7 - (today + datetime.timedelta(days=days_until_birthday)).weekday()

        if days_until_birthday <= 7:
            congratulation_date = today + datetime.timedelta(days=days_until_birthday)
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)