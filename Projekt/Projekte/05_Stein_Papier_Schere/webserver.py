from flask import Flask, render_template

app = Flask(__name__)
app.template_folder = 'templates'

# Funktion zum Lesen der Daten aus der Textdatei
def read_data():
    with open("anz.txt", "r") as file:
        data = file.readline().strip().split()
    return data

# Startseite anzeigen und Daten aus der Textdatei übergeben
@app.route('/')
def index():
    data = read_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
