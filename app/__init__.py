from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import boto3

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
s3 = boto3.client('s3')

from . import views, models

