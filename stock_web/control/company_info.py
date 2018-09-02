from flask import request, redirect, url_for, render_template, flash, session
from stock_web import app
from stock_web import db


@app.route('/company_info')
def company_info():
    return render_template('company_info.html')


@app.route('/search_symbol', methods=['POST'])
def search_symbol():
    symbol = request.form['symbol']
    if symbol == '':
        flash('銘柄を選択してください')
        return render_template('company_info.html')

    sql = "select * from mst_stock order by stock_code"
    result = db.engine.execute(sql).first()
    print(result)
    return render_template('company_info.html')