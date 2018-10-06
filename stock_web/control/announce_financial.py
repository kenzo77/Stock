from flask import request, redirect, url_for, render_template, flash, session
from stock_web.service import announce_financial_service
from stock_web import app


# 決算発表予定を取得します
@app.route('/announce_financial')
def announce_financial():
    result_list = announce_financial_service.get_announce_financial()
    return render_template('announce_financial.html', result_list=result_list, title="決算発表予定", mode=1)


# 決算発表結果 を取得します
@app.route('/financial_result')
def financial_result():
    result_list = announce_financial_service.get_financial_result()
    return render_template('announce_financial.html', result_list=result_list, title="決算発表結果", mode=2)


# 決算発表結果 を取得します
@app.route('/update_financial')
def update_financial():
    result_list = announce_financial_service.get_update_financial()
    return render_template('announce_financial.html', result_list=result_list, title="業績予想変更", mode=3)
