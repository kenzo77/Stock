from stock_web import db
from stock_web.dao import common_dao


# 銘柄検索を行います
def search_company(condition):
    base_sql =  "select "
    base_sql += "   substr(a.STOCK_CODE,1,4) as STOCK_CODE "
    base_sql += "   ,a.STOCK_NAME "
    base_sql += "   ,a.LISTED_PLACE "
    base_sql += "   ,c.BUSINESS_TYPE_NAME "
    base_sql += "   ,a.LIESTED_DATE "
    base_sql += "   ,b.CHARACTERISTIC "
    base_sql += " from MST_STOCK a "
    base_sql += "   inner join ( "
    base_sql += "      select * from MST_SHIKIHO s "
    base_sql += "      where (s.STOCK_CODE, s.GET_DATE) in ( "
    base_sql += "        select STOCK_CODE, max(GET_DATE) from MST_SHIKIHO group by STOCK_CODE) "
    base_sql += "   ) b on a.STOCK_CODE = b.STOCK_CODE "
    base_sql += "   inner join MST_BUSINESS_TYPE c "
    base_sql += "   on b.BUSINESS_TYPE = c.BUSINESS_TYPE "
    base_sql += " where a.IS_DELETE = 0 "
    result = db.engine.execute(base_sql)
    return common_dao.convert_json_list(result)