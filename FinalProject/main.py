from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import pandas as pd
import os

app = Flask(__name__)
df = pd.read_csv('user.csv')

# @app.route('/start')
#     return render_template("indexstart.html")


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    login = request.form
    userName = login['username']
    password = login['password']
    account = False

    if df['name'].str.contains(userName).any():
        account = True
    else:
        flash('Wrong Password!')

    if account:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return home()


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
