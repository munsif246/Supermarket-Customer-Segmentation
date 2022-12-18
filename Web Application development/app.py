import numpy as np
from flask import Flask, request, jsonify, render_template,redirect, url_for
import pickle

app = Flask(__name__) 
model = pickle.load(open('Kmeans2.pkl', 'rb')) 

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/service')
def service():
    return render_template('model.html')
    
@app.route('/analytics')
def analytics():
    return render_template('E_COMMERCE.html')
    
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/predict',methods=['GET','POST']) 
def predict():
    
    if request.method == 'POST':
        int_features = [float(x) for x in request.form.values()]#input values
        final_features = [np.array(int_features)] #coverting it to array 
        prediction = model.predict(final_features) #predicting
        
        x=""
        if(prediction==0):
            x="Cluster1"
        elif (prediction==1):
            x="Cluter2"
        elif (prediction==2):
            x="Cluter3"
        else:
            x="Cluter4"
        return render_template('model.html', prediction_text='The Cluter Customer belong to is {}'.format(x))
   

    


if __name__ == "__main__":
    app.run(debug=True)
    
