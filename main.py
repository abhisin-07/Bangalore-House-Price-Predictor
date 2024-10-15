from sys import breakpointhook
from flask import Flask,render_template,request
from matplotlib.backend_bases import LocationEvent
import pandas as pd
import pickle


app=Flask(__name__)
data=pd.read_csv('C:\\Users\\asus\\OneDrive\\Desktop\\python\\app\\Cleaned.csv')
pipe=pickle.load(open('C:\\Users\\asus\\OneDrive\\Desktop\\python\\app\\RidgeModel.pkl','rb'))
@app.route('/')
def index():
    locations=sorted(data['location'].unique())
    return render_template('index.html',locations=locations)
@app.route('/predict',methods=['POST'])
def predict():
    location=request.form.get('location')
    bhk=request.form.get('bhk')
    bath=request.form.get('bath')
    sqft=request.form.get('sqft')
    input=pd.DataFrame([[location,sqft,bath,bhk]],columns=['location','total_sqft','bath','bhk'])
    prediction=pipe.predict(input)[0].astype('float')
    
    
    return str(prediction)
if __name__ == "__main__":
    app.run(debug=True,port=5001)
 