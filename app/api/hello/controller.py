"""
a set of handlers for the hello api
controllers will run validation against the request, handle auth,
consume services/modules, and shape the response
"""

def handle_index():
    """index route"""
    return 'hello world'

def handle_name(name):
    """handle the name"""
    return 'hello ' + name
