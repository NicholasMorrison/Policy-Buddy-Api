"""
pytest suite to test the common tags route
common tags route should find and tag common terms that should be defined as
key points that stand out in the terms agreement
"""
# pylint: disable=redefined-outer-name
# pylint: disable=unused-import
from test.resource.client import client
ROUTE = '/test/common'

def test_post_method_enforced(client):
    """ test that get requests are rejected """
    response = client.get(ROUTE)
    assert response.status_code == 404
