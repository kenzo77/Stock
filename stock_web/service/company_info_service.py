from stock_web.dao import company_info_dao as dao


# 会社情報を取得します
def get_company_info(symbol):
    company_info = dao.get_company_info(symbol)
    result = dao.get_stock_performance(symbol)
    #Chart表示用に編集します
    labels = []
    sales_data = []
    operating_income_data = []
    ordinal_income_data = []
    net_income_data = []
    background_color_data = []
    border_color_data = []
    default_color = "rgba(0, 0, 255, 0.2)"
    expect_color = "rgba(255, 67, 66, 0.2)"
    default_border_color = "rgba(0, 0, 255, 1)"
    expect_border_color = "rgba(255, 67, 66, 1)"
    label_count = 1
    for perfomance in result:
        term = perfomance["TERM"]
        if term.find("予想") > 0:
            term = term[0:6] + '予想'
            if term in labels:
                label_count += 1
            labels.append(term + "_" + str(label_count))
            background_color_data.append(expect_color)
            border_color_data.append(expect_border_color)
        else:
            labels.append(term[0:6] + '実績')
            background_color_data.append(default_color)
            border_color_data.append(default_border_color)
        sales_data.append(perfomance["SALES"])
        operating_income_data.append(perfomance["OPERATING_INCOME"])
        ordinal_income_data.append(perfomance["ORDINARY_INCOME"])
        net_income_data.append(perfomance["NET_INCOME"])

    ohlc_labels = []
    ohlc_list = dao.get_ohlc_data(symbol)
    for data in ohlc_list:
        ohlc_labels.append(data["STOCK_DATE"])

    chart_data = {
        "labels": labels,
        "ohlc_labels": ohlc_labels,
        "ohlc_data": ohlc_list,
        "background_color_data": background_color_data,
        "border_color_data": border_color_data,
        "sales_data": ",".join(map(str, sales_data)),
        "operating_income_data": ",".join(map(str, operating_income_data)),
        "ordinal_income_data": ",".join(map(str, ordinal_income_data)),
        "net_income_data": ",".join(map(str, net_income_data))
    }
    return company_info, chart_data


if __name__ == '__main__':
    print(get_company_info("6501"))