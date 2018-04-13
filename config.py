import os

host = '0.0.0.0'
port = 8080
debug = True


CSRF_ENABLED = True

SECRET_KEY = 'suck my ass, little pidoras'

UPLOAD_FOLDER = 'uploads'

basedir = os.path.abspath(os.path.dirname(__name__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')  # CHANGE TO A DIFFERENT DB!

SQLALCHEMY_TRACK_MODIFICATIONS = False

