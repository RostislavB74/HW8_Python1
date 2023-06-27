from datetime import datetime, timedelta
from collections import defaultdict


users = [{'name': 'Dmitry Kryvsha', 'birthday': datetime(1988, 1, 1)},
         {'name': 'Leonid Chayka', 'birthday': datetime(1949, 12, 26)}]


def current_data():
    current_data = datetime(2022, 12, 20)  # datetime.now()
    return (current_data)


def get_bd(start, end, list_of_emp, current_year, current_date):
    result = defaultdict(list)
    for users in list_of_emp:
        bd = users["birthday"]
        if isinstance(bd, datetime):
            bd = bd.date()
        else:
            bd = datetime.strptime(bd, "%d-%m-%Y").date()
        if (end.year-start.year) > 0:
            bd = bd.replace(year=current_year)
            if (start <= bd <= end):
                if bd.weekday() in (5, 6):
                    bd = current_date + \
                        timedelta(days=7-(current_date.weekday()))

            else:
                bd = bd.replace(year=end.year)
                if (start <= bd <= end):
                    if bd.weekday() in (5, 6):
                        bd = current_date + \
                            timedelta(days=7-(current_date.weekday()))

            if bd.month == 2 and bd.day == 29 and not (current_year % 4 == 0 and
                                                       (current_year % 100 != 0 or
                                                        current_year % 400 == 0)):
                bd = bd.replace(day=1, month=3, year=current_year)
            bd = bd.replace(year=current_year)

            if start <= bd <= end:

                if bd.weekday() in (5, 6):
                    bd = current_date + \
                        timedelta(days=7-(current_date.weekday()))
                    print(result[bd].append(users['name']))
                    return result[bd].append(users['name'])
            else:
                print(result[bd].append(users['name']))
                return result[bd].append(users['name'])


def get_birthdays_per_week(list_of_emp: list) -> None:
    result = defaultdict(list)
    current_date = current_data().date()
    current_year = current_data().year
    start, end = get_period()
    result = get_bd(start, end, list_of_emp, current_year, current_date)
    print(result)


def get_period():  # -> tuple[datetime.date, datetime.date]:
    current_date = current_data()
    start_period = current_date + \
        timedelta(days=5-(current_date.weekday()))
    end_period = start_period + timedelta(18)

    return start_period.date(), end_period.date()


if __name__ == "__main__":
    for key, value in get_birthdays_per_week(users).items():
        # print(key)
        # print(value)
        result = sorted(get_birthdays_per_week(users).items())
        # print(result)
    for i in result:
        list1 = ', '.join(i[1])
        print(f'{i[0].strftime("%A")}: {list1}')
        # print(f'{result.key}:{result.value})')
        # print(f'{key.strftime("%A")}:', value)
        # print(sorted(get_birthdays_per_week(users).items()))
