"""
A set of handlers for the routes in the tags api
"""
from flask import request
from app.modules.lib.error import validation_error
from .validation import tags_validator

def handle_common_tags():
    """ controller function for tagging common phrases """
    is_valid, reasons = tags_validator.validate('common_tags', request)
    if not is_valid:
        return validation_error(reasons)
    return "common tag"
