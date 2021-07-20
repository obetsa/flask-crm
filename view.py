from app import app
from flask import render_template


@app.route('/')
def good():
    return render_template('index.html')


@app.route('/show_all')
def show_all():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM Departments').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)
