from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/after')
def about():
    return render_template("about.html")

@app.route('/before')
def before(): 
    return render_template("before.html");

@app.route('/nasa')
def nasa():
    return render_template("nasa.html")

@app.route('/team')
def team():
    return render_template("team.html")

if __name__ == '__main__':
    app.debug = True
    app.run()