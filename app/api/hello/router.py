""" a declaration of url paths for the hello api """

from flask import Blueprint
from app.api.hello import controller

router = Blueprint('hello', __name__)

router.add_url_rule('/hello', view_func=controller.handle_index)
router.add_url_rule('/hello/<name>', view_func=controller.handle_name)
