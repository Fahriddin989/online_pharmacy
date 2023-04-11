from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
babel = Babel()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    db.init_app(app)
    babel.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    from admin.routes import MyMainView
    from models import Medicines, Categories,Manufacturers,Active_substances,User
    from admin.views.medicines_view import MedicinesView


    admin = Admin(app, 'Baxtli-oila Apteka', index_view=MyMainView(),
                  template_mode='bootstrap4', url='/')

    admin.add_view(MedicinesView(Medicines, db.session))
    admin.add_view(ModelView(Categories, db.session))
    admin.add_view(ModelView(Manufacturers, db.session))
    admin.add_view(ModelView(Active_substances, db.session))
    admin.add_view(ModelView(User, db.session))

    return app
