from flask import current_app as app
from app.blueprints.auth import bp as auth
from app.blueprints.shop import bp as shop
from app.blueprints.api import bp as api
from app.blueprints.main import bp as main

app.register_blueprint(auth)
app.register_blueprint(shop)
app.register_blueprint(api)
app.register_blueprint(main)