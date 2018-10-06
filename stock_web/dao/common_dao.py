from stock_web import db


# 休日を取得します
def get_holidays(target):
    sql = "select * From MST_HOLIDAY where HOLIDAY > '{0}' order by HOLIDAY".format(str(target.year))
    result = db.engine.execute(sql)
    return convert_json_list(result)


# json形式に形成する
def convert_json_list(result):
    if result is None:
        return None

    ret = []
    for v in result:
        j = {}
        for col in v.items():
            j = {**j, **{col[0]: col[1]}}
        ret.append(j)
    return ret


if __name__ == '__main__':
    pass