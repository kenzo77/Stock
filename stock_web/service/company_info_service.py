from stock_web.dao import company_info_dao as dao


# 会社情報を取得します
def get_company_info(symbol):
    # company_info = dao.get_company_info(symbol)
    return dao.get_stock_performance(symbol)


if __name__ == '__main__':
    get_company_info("6501")