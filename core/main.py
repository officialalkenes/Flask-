import os
from pathlib import Path

from flask import Flask  # render_template, request, url_for, redirect

# from flask_sqlalchemy import SQLAlchemy
from core.db import db as database

from core.route.blog_routes import blog_bp


basedir = Path(__file__).resolve().parent.parent

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "newdb.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

database.init_app(app)

app.register_blueprint(blog_bp)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run()
