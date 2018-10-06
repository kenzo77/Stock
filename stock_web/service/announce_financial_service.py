from stock_web.dao import announce_financial_dao as dao
from stock_web.util import date_util
from datetime import datetime

# 決算発表情報を取得します
def get_announce_financial(add_days=20):
    if datetime.now().hour > 16:
        from_date = date_util.get_date(1)
    else:
        from_date = date_util.get_date()
    to_date = date_util.get_business_date(add_days=add_days)
    return dao.get_announce_financial(from_date, to_date)


# 決算発表結果を取得します
def get_financial_result(add_days=-20):
    from_date = date_util.get_date(add_days, date_format='{0:04d}/{1:02d}/{2:02d}')
    to_date = date_util.get_date(1, date_format='{0:04d}/{1:02d}/{2:02d}')
    return dao.get_financial_result(from_date, to_date, "決算短信")


# 業績予想変更を取得します
def get_update_financial(add_days=-20):
    from_date = date_util.get_date(add_days, date_format='{0:04d}/{1:02d}/{2:02d}')
    to_date = date_util.get_date(1, date_format='{0:04d}/{1:02d}/{2:02d}')
    return dao.get_financial_result(from_date, to_date, "業績予想")
