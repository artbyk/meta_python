from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_babel import Babel, lazy_gettext as _l

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# db = SQLAlchemy()
# migrate = Migrate()
bootstrap = Bootstrap(app)
login = LoginManager(app)
login.login_view = 'auth.login'
login.login_message = ('Please log in to access this page.')



# def create_app(config_class=Config):
#     app = Flask(__name__)
#     app.config.from_object(config_class)
#     db.init_app(app)
#     migrate.init_app(app, db)
#
#     bootstrap.init_app(app)
#     login.init_app(app)
#
#     from app.auth import bp as auth_bp
#     app.register_blueprint(auth_bp, url_prefix='/auth')
#
#     from app.main import bp as main_bp
#     app.register_blueprint(main_bp)
#
#     return app

from app import models
from app.auth import routes