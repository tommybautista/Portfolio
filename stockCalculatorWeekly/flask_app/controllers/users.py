from flask import Flask, render_template
from flask_app import app

@app.route('/')
def index():
    return render_template('/index.html')