from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        conn = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="1234",
            database="pass"
        )

        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (id, password) VALUES (%s, %s)",
            (username, password)
        )
        conn.commit()

        cursor.close()
        conn.close()
        return redirect(url_for("login"))
    
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        conn = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="1234",
            database="pass"
        )

        cursor = conn.cursor()
        cursor.execute(
            "SELECT id FROM users WHERE id = %s AND password = %s",
            (username, password)
        )
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user is not None:
            return render_template("index.html", username=user[0])

        return render_template("login.html", error="아이디 또는 비밀번호가 틀렸습니다.")
    
    return render_template("login.html")