from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('settings')

db = SQLAlchemy(app)

from author import models
from blog import views