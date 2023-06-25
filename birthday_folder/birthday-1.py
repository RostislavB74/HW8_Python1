from datetime import datetime, timedelta
from collections import defaultdict


users = [
    {'name': 'Rostyslav Bysko', 'birthday': datetime(1974, 4, 25)},
    {'name': 'Sergey Korchuk', 'birthday': datetime(1976, 7, 25)},
    {'name': 'Alexandr Korchuk', 'birthday': datetime(1984, 10, 20)},
    {'name': 'Viktor Bakharev', 'birthday': datetime(1962, 6, 23)},
    {'name': 'Svetlana Vratskaya', 'birthday': datetime(1974, 6, 24)},
    {'name': 'Fedor Bulko', 'birthday': datetime(1980, 6, 26)},
    {'name': 'Srgey Gudilin', 'birthday': datetime(1972, 2, 29)},
    {'name': 'Vladimir Metelev', 'birthday': datetime(1982, 12, 31)},
    {'name': 'Dmitry Kryvsha', 'birthday': datetime(1988, 1, 1)},
    {'name': 'Leonid Chayka', 'birthday': '26-6-1949'},
]


def get_bd(start, end, bd):
    if (start.day <= bd.day <= end.day):
        if (start.month <= bd.month <= end.month):
            bd = bd.replace(year=end.year)
        print(bd)
    return bd


def check_users(list_of_emp: list) -> None:
    result = defaultdict(list)
    current_date = current_data().date()
    current_year = current_data().year
    start, end = get_period()

    for users in list_of_emp:
        bd = users["birthday"]

        if isinstance(bd, datetime):
            bd = bd.date()
        else:
            bd = datetime.strptime(bd, "%d-%m-%Y").date()
        if bd.month == 2 and bd.day == 29 and not (current_year % 4 == 0 and
                                                   (current_year % 100 != 0 or
                                                    current_year % 400 == 0)):
            bd = bd.replace(day=1, month=3, year=current_year)
        bd = bd.replace(year=current_year)
        if (end.year-start.year) >= 1:
            # (get_bd(start, end, bd))
            bd = get_bd(start, end, bd)

        if start <= bd <= end:

            if bd.weekday() in (5, 6):
                bd = current_date + timedelta(days=7-(current_date.weekday()))
                result[bd].append(users['name'])
            else:
                result[bd].append(users['name'])

    return result


def current_data():
    current_data = datetime(2022, 12, 28)  # datetime.now()
    return (current_data)


def get_period():  # -> tuple[datetime.date, datetime.date]:
    current_date = current_data()
    start_period = current_date + \
        timedelta(days=5-(current_date.weekday()))

    return start_period.date(), (start_period + timedelta(8)).date()


if __name__ == "__main__":
    for key, value in check_users(users).items():
        print(key.strftime("%A"), value)
