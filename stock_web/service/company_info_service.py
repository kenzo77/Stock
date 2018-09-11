from stock_web.dao import company_info_dao as dao


# 会社情報を取得します
def get_company_info(symbol):
    # company_info = dao.get_company_info(symbol)
    result = dao.get_stock_performance(symbol)
    return convert_json_list(result)


# json形式に形成する
def convert_json_list(result):
    ret = []
    for v in result:
        j = {}
        for col in v.items():
            j = {**j, **{col[0]: col[1]}}
        ret.append(j)
    return ret


if __name__ == '__main__':
    get_company_info("6501")