from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "secret123"

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@123",
    database="portfolio"
)

cursor = db.cursor()

# Home Page
@app.route('/')
def home():
    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()
    return render_template('index.html', projects=projects)

# Contact Form
@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    cursor.execute(
        "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)",
        (name, email, message)
    )
    db.commit()
    return redirect('/')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == "admin" and request.form['password'] == "1234":
            session['admin'] = True
            return redirect('/admin')
    return render_template('login.html')

# Logout
@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect('/')

# Admin Panel
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if 'admin' not in session:
        return redirect('/login')

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        cursor.execute(
            "INSERT INTO projects (title, description) VALUES (%s, %s)",
            (title, description)
        )
        db.commit()

    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()

    return render_template('admin.html', projects=projects)

# Delete Project
@app.route('/delete/<int:id>')
def delete(id):
    if 'admin' not in session:
        return redirect('/login')

    cursor.execute("DELETE FROM projects WHERE id=%s", (id,))
    db.commit()
    return redirect('/admin')

if __name__ == "__main__":
    app.run(debug=True)