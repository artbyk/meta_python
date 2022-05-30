from flask import Flask, render_template, request, current_app, session
from flask_bootstrap import Bootstrap
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_babel import Babel, lazy_gettext as _l
# from flask_wtf.csrf import CsrfProtect as Csrf


# app = Flask(__name__)
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = _l('Please log in to access this page.')
babel = Babel()
# csrf = Csrf()



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    babel.init_app(app)
    # csrf.init_app(app)

    bootstrap.init_app(app)
    login.init_app(app)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app


@babel.localeselector
def get_locale():
    if request.args.get("languages"):
        print('lang = ', request.args.get('languages'))
        session['lang'] = request.args.get('languages')
    return session.get('lang', 'en')

from app import models
from app.auth import routes
