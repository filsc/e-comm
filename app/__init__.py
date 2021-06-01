from app import routes
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment 
from flask_login import LoginManger
from flask import Blueprint

#bp = Blueprint('main', __name__, static_folder='static',
 #              template_folder='templates')

bp = Blueprint('main', __name__, url_prefix='/')
db = SQLAlchemy()
migrate = Migrate()
momwnr = Moment()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app,db)
    moment.init_app(app)
    db = SQLAlchemy(app)
    migrate = Mrigrate(app, db)
    login_manager = LoginManager(app)
    moment = Moment(app)

    with app.app_context():
        # from . import models
        from app.blueprints.api import routes
        from app.blueprints.main import bp as main
        from .import register_blueprints
        #app.register_blueprint(main, url_prefix='/')

    return app
    
from .import routes, models