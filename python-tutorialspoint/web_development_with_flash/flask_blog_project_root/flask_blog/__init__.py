import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Absolute path to templates folder (cross-platform)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_FOLDER = os.path.join(BASE_DIR, "templates")

# Create Flask app with explicit template folder
app = Flask(__name__, template_folder=TEMPLATE_FOLDER)


app.config.from_object('settings')

db = SQLAlchemy(app)

print("Template folder:", app.template_folder)

from author import models
from author import views
from blog import views
