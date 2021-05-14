from flask import Flask, render_template, redirect, request
from mysqlconnection import MySQLConnection, connectToMySQL# import the function that will return an instance of a connection
app = Flask(__name__)

@app.route("/users")
def index():
    mysql= connectToMySQL('users_schema3')
    users= mysql.query_db('SELECT * FROM users;')
    return render_template("index.html", all_users=users)



@app.route("/users/new")
def index2():
    return render_template("Create.html")



@app.route("/users/new/create", methods=["POST"])
def create():
    mysql= connectToMySQL('users_schema3')
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(em)s, NOW(), NOW());"
    data = {
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "em": request.form["email"]
        
    }
    mysql.query_db(query,data)
    return redirect("/users")










if __name__ == "__main__":
    app.run(debug=True)