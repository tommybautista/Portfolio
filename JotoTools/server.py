from flask_app import app
from flask_app.controllers.tripPlanner import users,events
from flask_app.controllers.main import mainDashboards
from flask_app.controllers.tripBudget import tripBudgets

if __name__ == "__main__":
    app.run(debug=True)