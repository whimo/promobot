import os

host = '0.0.0.0'
port = 8080
debug = True


WTF_CSRF_ENABLED = False

UPLOAD_FOLDER = 'uploads'

basedir = os.path.abspath(os.path.dirname(__name__))
SQLALCHEMY_DATABASE_URI = 'postgresql://master:shaurma1337@dev-db.ca4wxh0ukzwc.us-east-1.rds.amazonaws.com:5428/pd'

SQLALCHEMY_TRACK_MODIFICATIONS = False
