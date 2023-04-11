import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///admin.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = os.urandom(20)

# Bootstrap themes https://bootswatch.com/4/
FLASK_ADMIN_SWATCH = 'cosmo'
BABEL_DEFAULT_LOCALE = 'ru'
# flatly
