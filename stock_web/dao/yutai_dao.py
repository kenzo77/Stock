from stock_web import db
from stock_web.dao import common_dao


# 優待情報を取得します
def get_yutai(month):
    sql = " select "
    sql += " substr(a.stock_code,1,4) as STOCK_CODE, "
    sql += " replace(replace(b.stock_name,'ＨＬＤＧ', ''), 'ＧＲＯＵＰ', '') as STOCK_NAME, "
    sql += " a.DIVIDENDS_DATE,"
    sql += " a.CONTENTS, "
    sql += " a.round_lot * c.end_price as MIN_VALUE_PRICE, "
    sql += " a.DIVIDENDS, "
    sql += " replace(b.DIVIDEND_RATE, '%', '') as DIVIDEND_RATE,  "
    sql += " round(cast(a.dividends as float) / (c.end_price * a.round_lot) * 100, 2) as YUTAI_RATE, "
    sql += " round(cast(REPLACE(B.DIVIDEND_RATE, '%', '') as decimal) + ROUND(CAST(A.DIVIDENDS AS FLOAT) / "
    sql += "   (C.END_PRICE * A.ROUND_LOT) * 100, 2), 2) as SUM_RATE, "
    sql += " b.LISTED_PLACE "
    sql += " From MST_YUTAI a "
    sql += "   inner join MST_STOCK b on a.stock_code = b.stock_code "
    sql += "   left outer join DATA_STOCKS_TODAY c on a.stock_code = c.stock_code "
    sql += " where a.dividends_date like '%{0}月%' "
    sql += " order by SUM_RATE desc, a.stock_code "


    result = db.engine.execute(sql.format(month))
    return common_dao.convert_json_list(result)