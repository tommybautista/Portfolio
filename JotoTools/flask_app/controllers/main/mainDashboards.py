from flask import Flask, render_template, redirect, request_started, session, request, flash
from flask_app import app

@app.route('/')
def mainDashboard():
    return render_template ("/main/mainDashboard.html")