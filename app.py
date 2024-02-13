from flask import Flask,render_template,request
import pickle
import numpy as np
app = Flask('__name__')
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    
    user_agent = request.headers.get('User-Agent')
    if 'Mozilla' in user_agent:  # Check if 'Mozilla' is present in the User-Agent header
        return render_template('index.html')
    else:
        return 'Hello, terminal user!'
    # return render_template('index.html')

@app.route('/predict',methods=["POST"])
def predict():
    feature=[int(x) for x in request.form.values()]
    feature_final=np.array(feature).reshape(-1,1)
    prediction=model.predict(feature_final)
    return render_template('index.html',prediction_text='Price of House will be Rs. {}'.format(int(prediction)))

if(__name__=='__main__'):
    app.run(debug=True, host='0.0.0.0', port='8080')

