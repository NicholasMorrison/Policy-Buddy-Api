""" a declaration of url paths for the hello api """

from flask import Blueprint
import controller

router = Blueprint('hello', __name__, url_prefix='/hello')

router.add_url_rule('/', view_func=controller.handle_index)
router.add_url_rule('/<name>', view_func=controller.handle_name)
