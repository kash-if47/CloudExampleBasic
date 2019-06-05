"""Cloud Foundry test"""
from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

print(os.getenv("PORT"))
port = int(os.getenv("PORT", 5000))

conn = sqlite3.connect('myDb.db')
print("Opened database successfully")
cur = conn.cursor()
cur.execute('select * from student')
rows = cur.fetchall()

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/list')
def list():
    # return 'Hello World! I am running on port ' + str(port)
    # d = data()
    return render_template("list.html",rows = rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
