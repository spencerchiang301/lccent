from flask import Flask, render_template
import pymysql
from config import Mysql_config

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/hello/<name>")
def hello(name):
    return render_template("hello.html", name=name)

def get_connection():
    return pymysql.connect(**Mysql_config)

@app.route("/employees")
def employees():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("select employee_id, first_name,last_name, salary from employees2;")
            rows = cursor.fetchall()
            employees = [
                {"employee_id":row[0],"first_name":row[1], "last_name":row[2], "salary":row[3]}
                for row in rows
            ]
            return render_template("employee.html", employees=employees)
    finally:
        conn.close()


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)