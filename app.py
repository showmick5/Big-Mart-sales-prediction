from flask import Flask, render_template, request
from flask import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('RF.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
   
    if request.method == 'POST':
        Item_Weight = float(request.form['Item_Weight'])
        Item_Visibility=float(request.form['Item_Visibility'])
        Item_Type=int(request.form['Item_Type'])
        Item_MRP = float(request.form['Item_MRP'])
        Outlet_Identifier=int(request.form['Outlet_Identifier'])
        Outlet_Size=int(request.form['Outlet_Size'])
        Outlet_Location_Type =int(request.form['Outlet_Location_Type'])
        Outlet_Type=int(request.form['Outlet_Type'])
        low_fat=int(request.form['low_fat'])
        prediction=model.predict([[Item_Weight,Item_Visibility,Item_Type,Item_MRP,Outlet_Identifier,Outlet_Size,Outlet_Location_Type,Outlet_Type,low_fat]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you have no sale")
        else:
            return render_template('index.html',prediction_text="store total sale is {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

