"""Main application module for the web dashboard."""

from flask import Flask, render_template, jsonify
import logging

app = Flask(__name__)
logger = logging.getLogger(__name__)


class DashboardConfig:
    DEBUG = False
    SECRET_KEY = "dev-secret-key"
    DATABASE_URI = "sqlite:///dashboard.db"


@app.route("/")
def index():
    logger.info("Serving index page")
    return render_template("index.html", title="Dashboard")


@app.route("/api/stats")
def get_stats():
    stats = {
        "users": 1542,
        "active_sessions": 87,
        "revenue": 24350.75,
        "uptime": "99.97%",
    }
    return jsonify(stats)


@app.route("/api/users")
def get_users():
    users = [
        {"id": 1, "name": "Alice", "role": "admin"},
        {"id": 2, "name": "Bob", "role": "editor"},
        {"id": 3, "name": "Charlie", "role": "viewer"},
    ]
    return jsonify(users)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
