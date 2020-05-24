"""
Common validator class
checkout the docs for validator.py from PyPI
https://validatorpy.readthedocs.io/en/latest/index.html
"""
from validator import validate as _validate

class RequestValidator:
    """
    A common class to implement validation on a Flask
    Request object after being constructed with a rule set
    """

    def __init__(self, rules):
        self.__rules = rules

    def get_rules(self):
        """ Getter function for rules set """
        return self.__rules

    def validate(self, rule, request):
        """
        validation function that will return a tuple in the form of
        success(Boolean), reasons(Dict or None)
        """

        ruleset = self.__rules.get(rule)
        if not ruleset:
            return False, 'The validation rule set does not exist'

        body_rules = ruleset.get('body')
        query_rules = ruleset.get('query')
        body = request.get_json()
        query = request.args

        if body_rules:
            status, reasons = _validate(body_rules, body)
            if not status:
                return status, reasons
        if query_rules:
            status, reasons = _validate(query_rules, query)
            if not status:
                return status, reasons
        return True, None
