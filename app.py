from flask import Flask
import sqlite3

application = Flask(__name__)

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("select * from people;")

people = cursor.fetchall()

@application.route("/")
def hello():
    return (f"<h1>Hello {people[0][0]} !</h1>")

if __name__ == "__main__":
    application.run(debug=True)