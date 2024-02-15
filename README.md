# Price Predictor API

This API predicts the price of a house based on input features, currently it takes only 1 feature which is area of the house.

## Getting Started

### Prerequisites

- Python 3.8 or above

### Installation

1. Clone the repository:
  - git clone "git@github.com:natesh-reddy/Price-Predictor-Server.git"
2. Change work directory -
  - cd "Price-Predictor-Server"
3. Install dependencies:
  - pip install -r requirements.txt

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
   - curl "http://localhost:8080/" - This will send a success message in return on terminal - "Hello, terminal user!"
   - Else navigate to http://localhost:8080 in your web browser to access the home page.
 


# Steps to deploy on EC2 instance and run testing pipeline -

1. Write the code for Rest API. I used flask server as my framework
2. Try to run it locally to check all the endpoints
3. Configure Test:
    - Install pytest
    - Write the code inside test_filename.py to create test methods
    - Command for testing - pytest
4. Configure Dockerhub:
    - Create an account on dockerhub where we can later the docker image which can pulled anywhere to run
5. Dockerise the Application:
    - Create Dockerfile to define the docker image for application
    - Build the docker - docker build -t <your_username>/my-private-repo .
    - Run it locally - docker run -d -p 8080:8080 <your_username>/my-private-repo
    - Push the docker image - docker push <your_username>/my-private-repo
6. Setup and Configure Circle CI:
    - Create account on Circle CI and connect your github. Add the private SSH key as well while connecting
    - Create a config.yml file in the .circleci directory. We have created one job to build the testing for installing dependencies and running Test
    - Push any changes to github to trigger the testing pipeline on Circle CI
7. Configure AWS-EC2 instance:
    - Create account on AWS and search for EC2 service
    - Launch an instance and make sure to allow all traffic in the security group. Also create a new ssh-key pair, or use an existing one if already created
8. Connect to EC2:
    - Locally check permission of rsa keys - ls -al pem_key_file
    - Change permission - chmod 600 pem_key_file
    - Connect - ssh -I pem_key_file ec2-user@ipaddress
9. Run docker on EC2:
    - Install docker -  sudo yum install docker
    - Open docker app - sudo service start docker
    - Check status - sudo service docker status
    - Check images - sudo docker images
    - Pull image - sudo docker pull image_name
    - Run docker - sudo docker run -d -p 80:8080 image_name
    - Check logs - sudo docker logs image_name/id
    - Check code - curl localhost:8080/
    - Now copy public ip of instance and check that on browser








