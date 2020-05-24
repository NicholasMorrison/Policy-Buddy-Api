""" a declaration of url paths for the definitions api """

from flask import Blueprint
from app.api.tags import controller

router = Blueprint('tags', __name__)

router.add_url_rule('/tags/common', methods=['POST'], view_func=controller.handle_common_tags)
