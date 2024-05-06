from flask import Flask, render_template


app = Flask(__name__)

##The routes are the url.

@app.route("/")
@app.route('/home')
def homePage():
    return render_template('base.html')