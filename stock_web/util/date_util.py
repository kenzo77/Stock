from stock_web.dao import common_dao as dao
import workdays
import monthdelta
from datetime import datetime


# 指定の営業日を取得します
def get_business_date(target=None, add_days=0):
    if target is None:
        target = datetime.now()
    if target.weekday() in (5, 6) and add_days == 0:
        add_days = 1
    str_target = "{0:04d}-{1:02d}-{2:02d}".format(target.year, target.month, target.day)

    # 休日を取得します
    holidays = []
    rows = dao.get_holidays(target)
    for row in rows:
        holiday = str(row['HOLIDAY'])
        if holiday == str_target and add_days == 0:
            add_days = -1
        date = holiday.split("-")
        holidays.append(datetime(year=int(date[0]), month=int(date[1]), day=int(date[2])))

    return workdays.workday(target, days=add_days, holidays=holidays)


# 年月日を取得します add_daysを指定すると、プラス営業日の日付を取得します
def get_date(add_days=0, date_format="{0:04d}-{1:02d}-{2:02d}"):
    now_date = datetime.now()
    business_days = get_business_date(now_date, add_days)
    return date_format.format(business_days.year, business_days.month, business_days.day)


# 文字列型の日付を日付型に変換します
def get_date_by_str_date(str_date, date_format='%Y/%m/%d'):
    return datetime.strptime(str_date, date_format)


# 日付型を文字列型に変換します
def get_str_date(date, date_format='%Y-%m-%d'):
    return date.strftime(date_format)


# 月の加減算を行います 文字列型の日付で返します
def get_add_month_date(date, delta, date_format='%Y/%m/%d'):
    dt = date + monthdelta.monthdelta(delta)
    return dt.strftime(date_format)


# format exsample
# '%Y-%m-%d' ⇒ '2012-12-29' default
# '%Y-%m-%d %H:%M:%S' ⇒ '2012-12-29 13:49:37'
def get_now_by_string(date_format='%Y-%m-%d'):
    return datetime.now().strftime(date_format)


if __name__ == '__main__':
    print(get_business_date(add_days=20))
