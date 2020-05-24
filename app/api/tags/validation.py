""" Request Validator for the tags api """
from validator import Required, Truthy, InstanceOf, Each
from app.modules.lib.request_validator import RequestValidator

tags_validator = RequestValidator({
    'common_tags': {
        'body': {
            'content': [Required, Truthy(), InstanceOf(list), Each([InstanceOf(str)])]
        }
    }
})
