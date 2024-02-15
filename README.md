# Price Predictor API

This API predicts the price of a house based on input features, currently it takes only 1 feature which is area of the house.

## Getting Started

### Prerequisites

- Python 3

### Installation

1. Clone the repository:
  - git clone https://github.com/your_username/price-predictor-api.git

### Usage
1. Start the Flask server:
  - python app.py
2. Navigate to http://localhost:8080 in your web browser to access the home page.
3. To make predictions, send a POST request to http://localhost:8080/predict with the required input features.


## API Documentation

### Endpoints
- Home: /

   - Method: GET
   - Description: Renders the home page of the application.

- Predict: /predict

   - Method: POST
   - Description: Predicts the price of a house based on input features.
   - Request Body: Form data containing the features.
      - Area (int): Size of house.
        
   - Response: HTML content with the predicted price of the house.

## Examples

- Predict
   - curl http://localhost:8080/ - This will send a success message in return on terminal - "Hello, terminal user!"
   - Else navigate to http://localhost:8080 in your web browser to access the home page.
