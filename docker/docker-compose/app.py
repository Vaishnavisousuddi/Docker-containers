from flask import Flask, request, render_template_string
import mysql.connector
import os

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "mysql-db"),
    user=os.getenv("MYSQL_USER", "root"),
    password=os.getenv("MYSQL_PASSWORD", "root"),
    database=os.getenv("MYSQL_DATABASE", "userdata")
)

# Create table if not exists
cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
)
""")
db.commit()

# HTML form template
form_html = """
<h2>User Registration</h2>
<form method="POST">
  Name: <input type="text" name="name" required><br>
  Email: <input type="email" name="email" required><br>
  <input type="submit" value="Submit">
</form>
{% if message %}
<p>{{ message }}</p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        db.commit()
        message = f"User {name} added successfully!"
    return render_template_string(form_html, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
