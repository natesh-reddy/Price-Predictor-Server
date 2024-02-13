FROM --platform=linux/amd64 python:3.12.1-bookworm AS build
# FROM python:3.12.1-bookworm

 

RUN mkdir -p "/home/Price-Predictor/house_predict"

RUN cd "/home/Price-Predictor/house_predict"
WORKDIR "/home/Price-Predictor/house_predict"
 
COPY . "/home/Price-Predictor/house_predict"
# COPY app.py "Price-Predictor/house_predict"

# COPY test_app.py "Price-Predictor/house_predict"

# COPY model.pkl "Price-Predictor/house_predict"

# COPY requirements.txt "/Price-Predictor/house_predict"

# COPY templates "/Price-Predictor/house_predict"

# COPY static "/Price-Predictor/house_predict"

RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]