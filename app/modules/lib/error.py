""" some functions to return consistent http error codes """

def validation_error(details='Unprocessable Entity'):
    """ Return a tuple with 422 status code """
    return details, 422

def not_found_error(details='Not Found'):
    """ Return a tuple with 404 status code """
    return details, 404

def bad_request_error(details='Bad Request'):
    """ Return a tuple with 400 status code """
    return details, 400
