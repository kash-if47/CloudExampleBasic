"""Cloud Foundry test"""
from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

print(os.getenv("PORT"))
port = int(os.getenv("PORT", 5000))



@app.route('/')
def home():
   return render_template('home.html')

@app.route('/student')
def student():
   return render_template('student.html')

@app.route('/delstudentpage')
def delstudentpage():
   return render_template('delstudentpage.html')

@app.route('/list')
def list():
    conn = sqlite3.connect('myDb.db')
    cur = conn.cursor()
    cur.execute('select * from student')
    rows = cur.fetchall()
    conn.close()
    return render_template("list.html",rows = rows)

@app.route('/delstudent',methods = ['POST', 'GET'])
def delstudent():
    id1 = request.form['id']
    con = sqlite3.connect('myDb.db')
    cur = con.cursor()
    cur.execute("DELETE from student where id = ?", (id1,))
    con.commit()
    cur.execute('select * from student')
    rows = cur.fetchall()
    con.close()
    return render_template("list.html", rows = rows)

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    id1 = request.form['id']
    ln = request.form['ln']
    fn = request.form['fn']
    add = request.form['add']
    cty = request.form['cty']
    eyr = request.form['eyr']
    nts = request.form['nts']
    con = sqlite3.connect('myDb.db')
    cur = con.cursor()
    cur.execute("INSERT INTO student (id,lastname,firstname,address,city,enrollmentyear,notes) VALUES (?,?,?,?,?,?,?)",(id1,ln,fn,add,cty,eyr,nts) )
    con.commit()
    con.close()
    cur = con.cursor()
    con = sqlite3.connect('myDb.db')
    cur.execute('select * from student')
    rows = cur.fetchall()
    con.close()
    return render_template("list.html", rows = rows)

         

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
