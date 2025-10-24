from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

db = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "mysql-db"),
    user=os.getenv("MYSQL_USER", "root"),
    password=os.getenv("MYSQL_PASSWORD", "root"),
    database=os.getenv("MYSQL_DATABASE", "testdb")
)

@app.route("/")
def index():
    cursor = db.cursor()
    cursor.execute("SELECT NOW()")
    result = cursor.fetchone()
    return f"Database time: {result[0]}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
