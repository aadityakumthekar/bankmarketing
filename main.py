import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from flask import Flask, render_template, request
app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))


@app.route('/')
def webpage():
    return render_template('webpage.html')
@app.route('/predict',methods = ['GET','POST'])
def predict():
    
    age = request.form.get('age')
    call_duration = request.form.get('call-duration')
    balance = request.form.get('balance')
    housing = request.form.get('housing')
    default = request.form.get('default')
    marital = request.form.get('marital-status')
    jobs= request.form.get('job')
    poutcome = request.form.get('poutcome')
    campaign = request.form.get('campaign')
    loan = request.form.get('loan')
    education = request.form.get('education')

    #headings =['age','default','balance','housing','loan','call_duration','campaign','jobs','marital','education','poutcome']
    arr=np.array([age,default,balance,housing,loan,call_duration,campaign,jobs,marital,education,poutcome])
    # arr = np.vstack([arr, new_row])
    #arr = np.insert(arr, 0, headings, axis=0)
    #preprocessing(arr)
    # print(arr)
    # prediction = model.predict([arr])
    # output = (prediction)
    # print(output)
    return render_template('index.html')
def preprocessing(arr):

    df = ['age', 'default', 'balance', 'housing', 'loan', 'duration', 'campaign',
       'pdays', 'previous', 'job_admin.', 'job_blue-collar',
       'job_entrepreneur', 'job_housemaid', 'job_management', 'job_retired',
       'job_self-employed', 'job_services', 'job_student', 'job_technician',
       'job_unemployed', 'job_unknown', 'marital_divorced', 'marital_married',
       'marital_single', 'education_primary', 'education_secondary',
       'education_tertiary', 'education_unknown', 'contact_cellular',
       'contact_telephone', 'contact_unknown', 'poutcome_failure',
       'poutcome_other', 'poutcome_success', 'poutcome_unknown']
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
