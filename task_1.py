from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d')
        today = datetime.today()
        diff = input_date - today
        return diff.days
    except ValueError:
        return "Неправильний формат дати"

print(get_days_from_today("2021-10-09"))