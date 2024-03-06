from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Verbindung zur SQLite-Datenbank herstellen
def connect_db():
    return sqlite3.connect('spielersymbole.db')

# Funktion zum Abrufen der Daten aus der Datenbank
def get_data():
    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM spielersymbole")
    data = cur.fetchall()
    con.close()
    return data

# Startseite anzeigen und Daten aus der Datenbank übergeben
@app.route('/')
def index():
    data = get_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
