from stock_web import db


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