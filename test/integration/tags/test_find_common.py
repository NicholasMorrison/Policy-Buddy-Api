"""
pytest suite to test the common tags route
common tags route should find and tag common terms that should be defined as
key points that stand out in the terms agreement
"""
# pylint: disable=redefined-outer-name
# pylint: disable=unused-import
from test.resource.client import client
ROUTE = '/tags/common'

def test_post_method_enforced(client):
    """ test that get requests are rejected """
    response = client.get(ROUTE)
    assert response.status_code == 405

def test_empty_body_rejected(client):
    """ test that a request with an empty body is rejected w/ validation error """
    response = client.post(ROUTE)
    assert response.status_code == 422

def test_body_content_string(client):
    """ test the validation of the content parameter in the body """
    response = client.post(ROUTE, json={
        'content': 'i should not be a string'
    })
    assert response.status_code == 422

def test_body_content_list(client):
    """ test that a list associated to the content body parameter is processible """
    response = client.post(ROUTE, json={
        'content': ['first paragraph', 'second paragraph']
    })
    print(response.data)
    assert response.status_code == 200
