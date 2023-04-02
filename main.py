import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from array import array
from flask import Flask, render_template, request
app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
#model1 = pickle.load(open('model1.pkl','rb'))

@app.route('/')
def webpage():
    return render_template('webpage.html')
@app.route('/predict',methods = ['POST'])
def predict():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        #to_predict_list = list(map(int, to_predict_list)) 
        #print(to_predict_list)    
        to_predict=preprocessing(to_predict_list)
        #prediction = model.predict(to_predict)
        #X_new = np.array([to_predict, to_predict**2, to_predict**3, to_predict**4, to_predict**5]).T
        prediction = model.predict(np.expand_dims(to_predict,axis=-1))
        print(prediction)





    # get list 
    # age = request.form.get('age')
    # call_duration = request.form.get('call-duration')
    # balance = request.form.get('balance')
    # housing = request.form.get('housing')
    # default = request.form.get('default')
    # marital = request.form.get('marital-status')
    # jobs= request.form.get('job')
    # poutcome = request.form.get('poutcome')
    # campaign = request.form.get('campaign')
    # loan = request.form.get('loan')
    # education = request.form.get('education')

    #headings =['age','default','balance','housing','loan','call_duration','campaign','jobs','marital','education','poutcome']
    #arr=np.array([age,default,balance,housing,loan,call_duration,campaign,jobs,marital,education,poutcome])
    # arr = np.vstack([arr, new_row])
    #arr = np.insert(arr, 0, headings, axis=0)
    #preprocessing(arr)
    # arr = [0.27272727, 0, 0.07689794, 1, 0, 0.07787719, 0, 0, 0, 0,1, 0, 0, 0, 0,0, 0, 0, 0, 0 ,0, 0, 1, 0, 1,0, 0, 0, 0, 0,1, 0,0, 0, 1]
    # arr_2d = np.array(arr).reshape(7,5)
    # prediction = model.predict(arr_2d)
    # output = (prediction)
    # print(output)

    return render_template('index.html')
def preprocessing(to_predict_list):
    a1=[0]*35
    for i in range(8):
        a1[i] = to_predict_list[i]
    for i in to_predict_list[9:-1]:
        a1[int(i)]=1    
    # Use map() to convert the strings to integers
    int_list = list(map(int, a1))

    # Use array() to create an array of integers
    int_array = np.array( int_list)
    return int_array


    
    
    # le = LabelEncoder()
    # arr['housing'] = le.fit_transform(arr['housing'])
    # arr['loan'] = le.fit_transform(arr['loan'])
    # arr['default'] = le.fit_transform(arr['default'])
    # print(arr)


if __name__ == '__main__':
    app.run(debug=True)
    





# Create a form in your Flask application that allows users to input their data. This form can be created using HTML and can be rendered using Flask's render_template function.

# Once the user submits the form, you can use Flask's request object to retrieve the data that was inputted. For example, if the form has fields for name and age, you can retrieve the values using the following code:

# python
