""" Flask App definition """

from flask import Flask
from .api import blueprints

app = Flask('app')
for blueprint in blueprints:
    app.register_blueprint(blueprint)
