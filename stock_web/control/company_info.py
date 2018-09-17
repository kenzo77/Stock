from flask import request, redirect, url_for, render_template, flash, session
from stock_web.service import company_info_service
from stock_web import app


@app.route('/company_info')
def company_info():

    return render_template('company_info.html')


@app.route('/search_symbol', methods=['GET', 'POST'])
def search_symbol():
    if request.method == 'POST':
        symbol = request.form['symbol']
        if symbol == '':
            flash('銘柄を選択してください')
            return render_template('company_info.html')
    else:
        symbol = request.values.get("symbol")

    company_info = company_info_service.get_company_info(symbol)
    print(company_info)
    return render_template('company_info.html', company_info=company_info)
