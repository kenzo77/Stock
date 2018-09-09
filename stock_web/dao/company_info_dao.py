from stock_web import db

def get_company_info(symbol):
    sql = "select * from mst_stock where stock_code like '{0}%' order by stock_code".format(symbol)
    result = db.engine.execute(sql).first()
    return result

if __name__ == '__main__':
    get_company_info()