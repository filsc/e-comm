from flask import currewnt_app as app
from app.blueprints.auth import bp as auth
fromblueprints.api import bp as api

app.register_blueprint(auth)
app.register_blueprint(api)