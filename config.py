import os

host = '0.0.0.0'
port = 8080
debug = True


WTF_CSRF_ENABLED = True
CSRF_ENABLED = True

SECRET_KEY = 'totally secret key'

UPLOAD_FOLDER = 'uploads'

basedir = os.path.abspath(os.path.dirname(__name__))
SQLALCHEMY_DATABASE_URI = 'postgresql://master:shaurma1337@***REMOVED***'

SQLALCHEMY_TRACK_MODIFICATIONS = False
