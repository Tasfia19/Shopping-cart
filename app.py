from calendar import month_name
import flask
from flask import Flask, redirect, render_template, request
import sqlite3
app = Flask(name)


@app.route('/')
@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    return render_template('index.html')
  else:
    name = request.form.get('Name')
    phone = request.form.get('password')

    connection = sqlite3.connect('login.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO tasfia(Name,password) VALUES(?,?)', (name, phone))
    connection.commit()
    connection.close()

    return "information stored successfully"
