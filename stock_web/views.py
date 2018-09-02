from flask import request, redirect, url_for, render_template, flash, session
from stock_web import db
from stock_web import app


@app.route('/')
def show_entries():
    if not session.get('logged_in'):
        return redirect('/login')
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        error = False
        if request.form['username'] == '':
            flash('ユーザ名は必須です')
            error = True
        if request.form['password'] == '':
            flash('パスワードは必須です')
            error = True

        if not error:
            session['logged_in'] = True
            flash('ログインしました')
            return render_template('home.html')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('ログアウトしました')
    return redirect(url_for('show_entries'))

