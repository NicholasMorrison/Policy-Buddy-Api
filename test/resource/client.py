"""
Defining a common flask test client as a
pytest fixture to be used by all integration tests
"""
import pytest
from app import app

@pytest.fixture
def client():
    """ flask app test client pytest fixture """
    test_client = app.test_client()
    return test_client
