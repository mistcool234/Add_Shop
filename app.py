from flask import Flask, render_template, request, redirect, session
import mysql.connector
from config import DB_CONFIG

app = Flask(__name__)
app.secret_key = 'tv_store_secret'

conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor(dictionary=True)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        cursor.execute("SELECT * FROM admin WHERE username=%s AND password=%s", (user, pwd))
        admin = cursor.fetchone()
        if admin:
            session['admin'] = user
            return redirect('/dashboard')
        return 'Invalid credentials'
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'admin' not in session:
        return redirect('/')
    cursor.execute("SELECT * FROM televisions")
    tvs = cursor.fetchall()
    return render_template('dashboard.html', tvs=tvs)

@app.route('/add', methods=['GET', 'POST'])
def add_tv():
    if 'admin' not in session:
        return redirect('/')
    if request.method == 'POST':
        brand = request.form['brand']
        model = request.form['model']
        price = request.form['price']
        desc = request.form['description']
        cursor.execute("INSERT INTO televisions (brand, model, price, description) VALUES (%s, %s, %s, %s)", (brand, model, price, desc))
        conn.commit()
        return redirect('/dashboard')
    return render_template('add_tv.html')

@app.route('/delete/<int:tv_id>')
def delete_tv(tv_id):
    cursor.execute("DELETE FROM televisions WHERE id=%s", (tv_id,))
    conn.commit()
    return redirect('/dashboard')

if __name__ == '__main__':
    app.run(debug=True)
