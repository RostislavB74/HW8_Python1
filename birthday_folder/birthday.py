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
    {'name': 'Leonid Chayka', 'birthday': datetime(1949, 6, 26)},
]


def get_period():  # -> tuple[datetime.date, datetime.date]:
    current_date = datetime.now()
    # datetime(2023, 2, 20)
    # print(current_date)  #
    start_period = current_date + \
        timedelta(days=5-(current_date.weekday()))
    return start_period.date(), (start_period + timedelta(10)).date()


def check_epl(list_of_emp: list) -> None:
    result = defaultdict(list)
    # print(type(result))
    current_date = datetime.now().date()
    current_year = datetime.now().year
    for users in list_of_emp:

        bd = users["birthday"]
        # print(bd)
        if isinstance(bd, datetime):
            bd = bd.date()
        else:
            bd = datetime.strptime(bd, "%d.%m.%Y").date()
        if bd.month == 2 and bd.day == 29 and not (current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0)):
            bd = bd.replace(day=1, month=3, year=current_year)
        bd = bd.replace(year=current_year)
        # print(bd)
        start, end = get_period()
        # print(result.items())
        if start <= bd <= end:
            # print(bd.day)
            if bd.weekday() in (5, 6):
                # print(bd.weekday())
                # bd.weekday = datetime.'Monday'
                bd = current_date + timedelta(days=7-(current_date.weekday()))
                result[bd].append(users['name'])
                # print(bd)
            else:
                result[bd].append(users['name'])

    return result


if __name__ == "__main__":
    for key, value in check_epl(users).items():
        # print(value)
        print(key.strftime("%A"), value)
        # print(key, value)
    # print(get_period())
