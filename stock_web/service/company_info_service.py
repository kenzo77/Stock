from stock_web.dao import company_info_dao as dao


# 会社情報を取得します
def get_company_info(symbol):
    result = dao.get_stock_performance(symbol)
    #Chart表示用に編集します
    labels = []
    sales_data = []
    operating_income_data = []
    ordinal_income_data = []
    net_income_data = []
    label_count = 1
    for p in result:
        term = p["TERM"]
        if term.find("予想") > 0:
            term = term[0:6] + '予想'
            if term in labels:
                label_count += 1
            labels.append(term + "_" + str(label_count))
        else:
            labels.append(term[0:6] + '実績')
        sales_data.append(p["SALES"])
        operating_income_data.append(p["OPERATING_INCOME"])
        ordinal_income_data.append(p["ORDINARY_INCOME"])
        net_income_data.append(p["NET_INCOME"])

    chart_data = {
        "labels": labels,
        "sales_data": ",".join(map(str, sales_data)),
        "operating_income_data": ",".join(map(str, operating_income_data)),
        "ordinal_income_data": ",".join(map(str, ordinal_income_data)),
        "net_income_data": ",".join(map(str, net_income_data)),
    }
    return chart_data


if __name__ == '__main__':
    print(get_company_info("6501"))