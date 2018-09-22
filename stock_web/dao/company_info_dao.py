from stock_web import db
from stock_web.dao import common_dao

# 会社情報を取得します
def get_company_info(symbol):
    sql = "select * from mst_stock where stock_code = '{0}-T' order by stock_code".format(symbol)
    result = db.engine.execute(sql).first()
    return common_dao.convert_json_list(result)


# 会社の業績を取得します
def get_stock_performance(symbol):
    sql = "select distinct TERM, SALES / 1000000 as SALES, OPERATING_INCOME / 1000000 as OPERATING_INCOME, " \
          " ORDINARY_INCOME / 1000000 as ORDINARY_INCOME, NET_INCOME / 1000000  as NET_INCOME" \
          " From MST_PERFORMANCE where Stock_code = '{0}-T' and term not like '%Q%' and " \
          "(term like '%会社実績%' or term like '%会社予想%') order by term, announce_date".format(symbol)
    result = db.engine.execute(sql)
    return common_dao.convert_json_list(result)

if __name__ == '__main__':
    print(get_company_info('1301'))
