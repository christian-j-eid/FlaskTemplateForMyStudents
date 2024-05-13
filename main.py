from flask import Flask, render_template


app = Flask(__name__)

##The routes are the url.

@app.route("/")
@app.route('/home')
def homePage():
    return render_template('base.html')

@app.route('/students')
def students():
    items = [
        {'id': 1, 'name': 'Christian', 'c': 'orange', 'price': 100000},
        {'id': 2, 'name': 'Kai', 'c': 'red', 'price': 500},
        {'id': 3, 'name': 'Noah', 'c': 'yellow', 'price': 500},
    ]

    return render_template('students.html', items = items )