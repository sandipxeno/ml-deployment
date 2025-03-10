import pytest
from app import app  # Import the Flask application from the app module

@pytest.fixture
def client():
    """
    Pytest fixture to create a test client for the Flask app.
    This allows us to send requests to the app without running the server.
    """
    with app.test_client() as client:
        yield client  # Provides the test client for use in tests

def test_home(client):
    """
    Test case for the home route ('/').
    - Sends a GET request to the home route.
    - Checks if the response status code is 200 (OK).
    - Verifies that the response JSON matches the expected output.
    """
    response = client.get("/")  # Send a GET request to the home route
    assert response.status_code == 200  # Ensure the response is successful
    assert response.get_json() == {"message": "Hello, Inference!"}  # Verify the expected JSON response

