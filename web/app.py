from flask import Flask, request, jsonify, render_template_string
import mysql.connector
import os

app = Flask(__name__)

HTML_FORM = """
<!doctype html>
<title>Dateneingabe</title>
<h1>Neuen Eintrag hinzufügen</h1>
<form action="/submit" method="post">
  <input type="text" name="name" placeholder="Name eintragen" required>
  <input type="submit" value="Absenden">
</form>
<hr>
<h2>Gespeicherte Einträge:</h2>
<ul>
  {% for item in items %}
    <li>{{ item.id }} – {{ item.name }}</li>
  {% endfor %}
</ul>
"""

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST', 'db'),
        user=os.getenv('DB_USER', 'user'),
        password=os.getenv('DB_PASSWORD', 'password'),
        database=os.getenv('DB_NAME', 'appdb')
    )

@app.route('/', methods=['GET'])
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name FROM items")
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template_string(HTML_FORM, items=items)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (name) VALUES (%s)", (name,))
    conn.commit()
    cursor.close()
    conn.close()
    return 'Eintrag gespeichert! <a href="/">Zurück</a>'


@app.route('/data', methods=['POST'])
def insert_data():
    content = request.json
    name = content.get('name')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (name) VALUES (%s)", (name,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"status": "success", "name": name})

@app.route('/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name FROM items")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)
