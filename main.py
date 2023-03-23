import pickle
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def webpage():
    return render_template('webpage.html')

def predict():
    prediction = model.predict([request.form.get('age','job','duration','')])
    output = (prediction)
    print(output)


if __name__ == '__main__':
    app.run(debug=True)


# def get_function():
#     age = request.form.get('age')
    





# Create a form in your Flask application that allows users to input their data. This form can be created using HTML and can be rendered using Flask's render_template function.

# Once the user submits the form, you can use Flask's request object to retrieve the data that was inputted. For example, if the form has fields for name and age, you can retrieve the values using the following code:

# python
