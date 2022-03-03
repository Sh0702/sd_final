from os import stat
import re
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', status=True)


@app.route('/home')
def home():
    username = request.args.get('username')
    password = request.args.get('password')

    connection = sqlite3.connect('sanj.db')
    con = connection.cursor()

    users = list(con.execute('select * from user'))
    con.close
    connection.close
    for user in users:
        if user[1] == username and user[2] == password:
            return render_template('home.html')
    return render_template('index.html', status=False)


@app.route('/ticket')
def ticket():
    movie = request.args.get('movie')
    date = request.args.get('date')
    timing = request.args.get('timing')

    connection = sqlite3.connect('sanj.db')
    con = connection.cursor()

    con.execute('insert into movie (name, date, timing) values (\'{}\', \'{}\', \'{}\')'.format(
        movie, date, timing))
    details = list(con.execute('select * from movie'))
    connection.commit()
    return render_template('ticket.html', details=details)


if __name__ == '__main__':
    app.run(debug=True)