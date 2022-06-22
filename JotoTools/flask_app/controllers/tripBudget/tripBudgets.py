from flask import Flask, render_template, redirect, request_started, session, request, flash
from flask_app import app

@app.route('/indexTripBudget')
def indexTripBudget():
    return render_template ("/tripBudget/dashboardTripBudget.html")