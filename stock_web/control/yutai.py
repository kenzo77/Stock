from flask import request, redirect, url_for, render_template, flash, session
from stock_web.service import yutai_service
from stock_web import app
from stock_web.util import date_util

# 優待情報を取得します
@app.route('/yutai', methods=['GET'])
def yutai():
    if len(request.values) == 0:
        month = date_util.get_business_date().month
    else:
        month = request.values.get("month")
    result_list = yutai_service.get_yutai(month)
    return render_template('yutai_list.html', result_list=result_list, title="優待情報", month=month)
