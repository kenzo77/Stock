from stock_web.dao import yutai_dao as dao


# 業績予想変更を取得します
def get_yutai(month):
    return dao.get_yutai(month)
