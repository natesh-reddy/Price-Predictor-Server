import pytest
from app import app as flask_app

@pytest.fixture
def app():
    """Yield your Flask application for testing."""
    yield flask_app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

# Assuming the rest of the setup is similar...

def test_predict_route(client):
    """Test the /predict route using the actual predict function."""
    # Provide valid form data that matches what your model expects
    # This example assumes your model expects a single feature named 'feature1'
    form_data = {'area': '10'}  # Adjust the form data as necessary

    response = client.post('/predict', data=form_data)
    assert response.status_code == 200
    # Check for a specific part of the response that indicates a successful prediction
    assert b'Price of House will be Rs.' in response.data

    # If you know the expected prediction outcome for the given input, include it in your assertion
    # For example, if inputting 'feature1': '5' is expected to predict a price of 123456, assert that
    expected_prediction = '15000'  # Adjust based on the expected outcome for your test data
    expected_response = f'Price of House will be Rs. {expected_prediction}'.encode()
    assert expected_response in response.data, "The prediction value does not match the expected output"

