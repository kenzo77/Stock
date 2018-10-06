from stock_web import db
from stock_web.dao import common_dao


# 会社情報を取得します
def get_company_info(symbol):
    sql = "SELECT "
    sql += "      substr(a.STOCK_CODE, 1, 4) as STOCK_CODE "
    sql += "    , a.STOCK_NAME "
    sql += "    , c.BUSINESS_TYPE_NAME "
    sql += "    , replace(b2.ESTABLISHED, '.', '/') as ESTABLISHED "
    sql += "    , a.LIESTED_DATE "
    sql += "    , a.LISTED_PLACE "
    sql += "    , a.FISCAL_PERIOD "
    sql += "    , ROUND(cast(a.SHARED_OUTSTANDING * e.end_price as decimal) / 100000000) as TOTAL_MARKET_VALUE "
    sql += "    , ROUND(cast(e.end_price as float) / cast(g.net_income / a.SHARED_OUTSTANDING as float), 3) as PER "
    sql += "    , ROUND(cast(e.end_price as float) / cast(a.BPS as float), 3) as PBR"
    sql += "    , b2.CHARACTERISTIC "
    sql += "    , a.COMPANY_PROFILE "
    sql += "    , b2.CONSOLIDATED_BUSINESS "
    sql += "    , b2.COMMENTARY1 "
    sql += "    , b2.COMMENTARY2 "
    sql += "    , b2.EMPLOYEE "
    sql += "    , b2.STOCK_FOREIGN_RATIO "
    sql += "    , b2.STOCK_INVESTMENT_RATIO "
    sql += "    , b2.FREE_FLOATWEIGHT "
    sql += "    , b2.SPECIFIC_SHAREHOLDER_RATIO "
    sql += "    , b2.PRINCIPAL_SHAREHOLDER "
    sql += "    , b2.OFFICER "
    sql += "    , a.DIVIDEND_RATE "
    sql += "    , d.REMARK "
    sql += "    , d.DIVIDENDS_DATE "
    sql += "    , d.DIVIDENDS "
    sql += "    , ROUND(d.DIVIDENDS / cast(e.END_PRICE  * d.ROUND_LOT as  float) * 100, 2) as YUTAI_RATIO "
    sql += "    , e.END_PRICE "
    sql += "    , b2.ASSETS "
    sql += "    , b2.EQUITY "
    sql += "    , ROUND(cast(b2.EQUITY_RATIO as float) * 100, 2) as EQUITY_RATIO "
    sql += "    , b2.CAPITAL_STOCK "
    sql += "    , b2.RETURNED_EARNINGS "
    sql += "    , b2.LIABILITIES_WITH_INTEREST "
    sql += "    , b2.COMPETITORS as LAST_COMPETITORS "
    sql += "    , f.COMPETITORS as COMPETITORS "
    sql += "    , b2.URL "
    sql += "FROM MST_STOCK a "
    sql += "    left outer join ( select * from MST_SHIKIHO a where (a.stock_code, a.get_date) in ( "
    sql += "      select b.stock_code, max(b.get_date) from MST_SHIKIHO b group by b.stock_code "
    sql += "    )) b2 on a.stock_code  = b2.stock_code "
    sql += "    left outer join ( select * from MST_SHIKIHO a where (a.stock_code, a.get_date) in ( "
    sql += "      select b.stock_code, min(b.get_date) from MST_SHIKIHO b group by b.stock_code "
    sql += "    )) f on a.stock_code  = f.stock_code "
    sql += "    left outer join MST_BUSINESS_TYPE c on b2.BUSINESS_TYPE  = c.BUSINESS_TYPE "
    sql += "    left outer join MST_YUTAI d on a.stock_code  = d.stock_code  "
    sql += "    left outer join DATA_STOCKS_TODAY e on a.stock_code  = e.stock_code  "
    sql += "    left outer join ( select * From MST_PERFORMANCE a where (a.stock_code, a.term, a.announce_date) in ( "
    sql += "      select b.stock_code, max(b.term), max(b.announce_date) from MST_PERFORMANCE b "
    sql += "      where b.term  like '%会社予想' group by b.stock_code "
    sql += "    )) g on a.stock_code  = g.stock_code "
    sql += "WHERE a.STOCK_CODE = '{0}-T'".format(symbol)
    result = db.engine.execute(sql)
    result_list = common_dao.convert_json_list(result)
    if result_list and len(result_list) > 0:
        return result_list[0]
    return None

# 会社の業績を取得します
def get_stock_performance(symbol):
    sql = "select distinct TERM, SALES / 1000000 as SALES, OPERATING_INCOME / 1000000 as OPERATING_INCOME, " \
          " ORDINARY_INCOME / 1000000 as ORDINARY_INCOME, NET_INCOME / 1000000  as NET_INCOME" \
          " From MST_PERFORMANCE where Stock_code = '{0}-T' and term not like '%Q%' and " \
          "(term like '%会社実績%' or term like '%会社予想%') order by term, announce_date".format(symbol)
    result = db.engine.execute(sql)
    return common_dao.convert_json_list(result)


# 日足データを取得します
def get_ohlc_data(symbol):
    sql = "SELECT * FROM (SELECT STOCK_DATE, START_PRICE, HIGH_PRICE, LOW_PRICE, END_PRICE, VOLUME " \
          "FROM DATA_STOCKS WHERE STOCK_CODE = '{0}-T' ORDER BY STOCK_DATE desc limit 60) " \
          "ORDER BY STOCK_DATE desc".format(symbol)
    result = db.engine.execute(sql)
    return common_dao.convert_json_list(result)


if __name__ == '__main__':
    print(get_company_info('1301'))
