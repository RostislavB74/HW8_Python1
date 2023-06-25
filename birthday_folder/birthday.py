from datetime import datetime, timedelta
from collections import defaultdict


users = [
    {'name': 'Rostyslav Bysko', 'birthday': '1974-4-25'},
    {'name': 'Sergey Korchuk', 'birthday': datetime(1976, 7, 25)},
    {'name': 'Alexandr Korchuk', 'birthday': datetime(1984, 10, 20)},
    {'name': 'Viktor Bakharev', 'birthday': datetime(1962, 6, 23)},
    {'name': 'Svetlana Vratskaya', 'birthday': datetime(1974, 6, 24)},
    {'name': 'Fedor Bulko', 'birthday': '1980-6-26'},
    {'name': 'Srgey Gudilin', 'birthday': datetime(1972, 2, 29)},
    {'name': 'Vladimir Metelev', 'birthday': datetime(1982, 12, 31)},
    {'name': 'Dmitry Kryvsha', 'birthday': datetime(1988, 1, 1)},
    {'name': 'Leonid Chayka', 'birthday': '1949-6-26'},
]
# def get_birthdays_per_week(name, birthday):


def check_users(list_of_emp: list) -> None:
    result = defaultdict(list)
    current_year = datetime.now().year
    for users in list_of_emp:
        bd = users["birthday"]
        if isinstance(bd, datetime):
            bd = bd.date()

        else:
            bd = datetime.strptime(bd, "%Y-%m-%d").date()
        bd = bd.replace(year=current_year)

        start, end = get_period()

        if start <= bd <= end:
            if bd.weekday() in (5, 6):
                result[bd].append(users["name"])
            else:
                result[bd].append(users["name"])
    return result


def get_period():  # -> tuple[datetime.date, datetime.date]
    current_date = datetime.now()  # 2023-06-24
    start_period = current_date + \
        timedelta(days=5-current_date.weekday())  # timedelta =0
    # end_period= 2023-06-30
    return start_period.date(), (start_period + timedelta(6)).date()


# for elem in users:
# print(elem.values())


if __name__ == "__main__":
    for key, value in check_users(users).items():
        print(key.strftime("%A"), value)
