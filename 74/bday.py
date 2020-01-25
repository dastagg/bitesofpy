import calendar


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    date = str(date)
    y, m, d = date.split("-")
    y = int(y)
    m = int(m)
    d = int(d)
    dow = calendar.weekday(y, m, d)
    d_name = calendar.day_name[dow]

    return d_name
