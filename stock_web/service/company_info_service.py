from stock_web.dao import company_info_dao as dao

def get_company_info(symbol):
    return dao.get_company_info(symbol)

if __name__ == '__main__':
    pass