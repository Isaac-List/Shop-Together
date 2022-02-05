from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


app = Flask(__name__)
  
file_path = os.path.abspath(os.getcwd()) + "items.db"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + file_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)
mm = Marshmallow(app)
