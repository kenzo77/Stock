from stock_web import db
from stock_web.dao import common_dao


# 今後の決算発表情報を取得します
def get_announce_financial(from_date, to_date):
    sql = "select "
    sql += " substr(a.STOCK_CODE,1,4) as STOCK_CODE, "
    sql += " replace(replace(b.STOCK_NAME,'ＨＬＤＧ', ''), 'ＧＲＯＵＰ', '') as STOCK_NAME, "
    sql += " a.ANNOUNCE_DATE, "
    sql += " a.FINANCIAL_TYPE, "
    sql += " b.LISTED_PLACE, "
    sql += " cast(cast(e.SALES as float) / f.SALES * 100 as int) as PROGRESS_SALES_RATIO, "
    sql += " cast(cast(e.OPERATING_INCOME as float) / f.OPERATING_INCOME * 100 as int) as PROGRESS_OPE_RATIO, "
    sql += " cast(cast(e.ORDINARY_INCOME as float) / f.ORDINARY_INCOME * 100 as int) as PROGRESS_ORD_RATIO, "
    sql += " cast(cast(e.NET_INCOME as float) / f.NET_INCOME * 100 as int) as PROGRESS_INCOME_RATIO, "
    sql += " round((cast(g.OPERATING_INCOME - f.OPERATING_INCOME as float) / f.OPERATING_INCOME) * 100, 1) as SHIKIHO_DIFF_RATIO "
    sql += "from MST_ANNOUNCE_FINANCIAL a"
    sql += " left outer join MST_STOCK b on a.stock_code = b.stock_code"
    sql += " left outer join ("
    sql += "  select * from MST_PERFORMANCE c"
    sql += "  where (c.stock_code, c.term) in "
    sql += "   (select d.stock_code, max(d.term) from MST_PERFORMANCE d "
    sql += "    where d.term like '%会社実績%' group by d.stock_code)"
    sql += " ) e on e.stock_code = a.stock_code"
    sql += " left outer join ("
    sql += "  select * from MST_PERFORMANCE c"
    sql += "  where (c.stock_code, c.term, c.announce_date) in (select d.stock_code, max(d.term), max(d.announce_date)"
    sql += "    from MST_PERFORMANCE d where d.term like '%会社予想%' group by d.stock_code)"
    sql += " ) f on f.stock_code = e.stock_code and substr(f.term, 1, 6) > substr(e.term, 1, 6) "
    sql += " left outer join ( "
    sql += "   select b.stock_code, b.term, b.sales, b.operating_income, b.ordinary_income, b.net_income, b.eps "
    sql += "   from MST_PERFORMANCE b  "
    sql += "   where b.term like '%四季報予想%'  "
    sql += "   and (b.stock_code, b.announce_date) in ( "
    sql += "     select a.stock_code, max(a.announce_date) From MST_PERFORMANCE a "
    sql += "     where a.term like '%四季報予想%' group by a.stock_code "
    sql += "   ) "
    sql += " ) g on g.stock_code = f.stock_code and substr(g.term,1, 6) = substr(f.term,1, 6) "
    sql += " where trim(a.ANNOUNCE_DATE) between '{0}' and '{1}'"
    sql += " order by a.ANNOUNCE_DATE, a.FINANCIAL_TYPE, STOCK_CODE"

    result = db.engine.execute(sql.format(from_date, to_date))
    return common_dao.convert_json_list(result)


# 決算発表結果情報を取得します
def get_financial_result(from_date, to_date, search_word):
    sql = " select"
    sql += "  substr(a.ANNOUNCED_DATE,1, 10) as ANNOUNCED_DATE"
    sql += " ,a.STOCK_CODE"
    sql += " ,trim(a.stock_name) as STOCK_NAME "
    sql += " ,a.TITLE "
    sql += " ,a.LINK "
    sql += " ,a.NET_SALES "
    sql += " ,a.OPERATING_INCOME "
    sql += " ,a.ORDINARY_INCOME "
    sql += " ,a.NET_INCOME "
    sql += " ,a.CHANGE_SALES "
    sql += " ,a.CHANGE_OPERATING "
    sql += " ,a.CHANGE_ORDINARY "
    sql += " ,a.CHANGE_NET_INCOME "
    sql += " ,a.PROGRESS_SALES "
    sql += " ,a.PROGRESS_OPERATING "
    sql += " ,a.PROGRESS_ORDINARY "
    sql += " ,a.PROGRESS_NET_INCOME "
    sql += " ,a.CHANGE_REASON "
    sql += " From DATA_TDnet a   "
    sql += " Where '{0}' <= a.announced_date and a.announced_date <='{1}'"
    sql += " And title like '%{2}%' and title not like '%補足%'"
    sql += " Order by substr(a.ANNOUNCED_DATE,1, 10) desc, a.stock_code "

    result = db.engine.execute(sql.format(from_date, to_date, search_word))
    return common_dao.convert_json_list(result)


if __name__ == '__main__':
    print(get_announce_financial('2018-10-01', '2018-10-31'))
