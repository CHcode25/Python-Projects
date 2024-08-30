from flask import Flask,render_template,url_for, redirect,request
from sqlalchemy import create_engine, text
import sqlite3
import logging

app = Flask(__name__)

engine = create_engine("sqlite:///roster.db")

@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/delete", methods=["POST","GET"])
def deleterec():
    if request.method == "POST":
        nm = request.form.get("nm")
        with engine.connect() as connection:
         connection.execute(text(f"DELETE FROM students WHERE name='{nm}';"))
         connection.commit()
         connection.close()
         message = "Success"
         return render_template("deleteresult.html", message=message)
    else:
      request.method == "GET"
      return render_template("delete.html")

@app.route("/update",methods=["POST","GET"])
def updaterec():
    if request.method == "POST":
        nm = request.form.get("nm")
        addr = request.form.get("add")
        city = request.form.get("city")
        id = request.form.get("id")
        with engine.connect() as connection:
         rows= connection.execute(text(f'INSERT INTO students (name, addr, city,id) VALUES ("{nm}","{addr}","{city}","{id}");'))
         connection.commit()
         connection.close()
         message = (f"{nm},has been added successfully")
         return render_template("updateresult.html", message=message)
    
    else:
      request.method == "GET"
      return render_template("update.html")


@app.route("/view", methods=["GET"])
def view_page():
    if request.method == "GET":
        with engine.connect() as connection:
         rows= connection.execute(text("SELECT * FROM students"))
         connection.close()
         return render_template("view.html", rows=rows)
        
    else:
      return render_template("view.html")

@app.route("/search", methods=["POST","GET"])
def searchrec():
    if request.method == "POST":
        if request.method == "POST":
         name = request.form.get("nm")
         city = request.form.get("city")

        with engine.connect() as connection:
         rows = connection.execute(text(f"SELECT * FROM students WHERE name='{name}' AND city='{city}';"))
         connection.close()
         return render_template("searchresult.html", rows=rows)
  
    
    else:
      request.method == "GET"
      return render_template("search.html")

if __name__ == '__main__':
    app.run(debug=True)
