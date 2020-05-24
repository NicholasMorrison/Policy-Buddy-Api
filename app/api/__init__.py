""" a complete catalog of all blueprints for the api """

from .hello import hello_blueprint
from .tags import tags_blueprint

blueprints = [
    hello_blueprint,
    tags_blueprint
]
