from datetime import date, time, datetime


def diff_dates(recorddate):
    print(recorddate)
    now = datetime.now()
    d1 = date(now.year, now.month, now.day)
    d2 = date(recorddate.year, recorddate.month, recorddate.day)
    return abs(d1 - d2).days
