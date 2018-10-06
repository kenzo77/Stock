from flask import request, redirect, url_for, render_template, flash, session
from stock_web.service import search_company_service
from stock_web import app


@app.route('/search_company_init')
def search_company_init():
    return render_template('search_company.html', val=[{"symbol": ""}, {"symbol": ""}, {"symbol": ""}], title="会社検索")


@app.route('/search_company', methods=['POST'])
def search_company():
    company_list = search_company_service.search_company(request.form)
    return render_template('search_company.html', company_list=company_list, val=request.form, title="会社検索")