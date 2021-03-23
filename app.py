from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
app = Flask(__name__, template_folder = 'template')

model = pickle.load(open("svm_tuned105.pkl", "rb"))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        ssc_p = request.form['ssc_p']
        board_type=request.form['board_type']
        '''if board_type == 'Central-Board':
            board_type==0
        else:
            board_type==1
        '''
        hsc_p = float(request.form['hsc_p'])
        hscboard_type=request.form['hscboard_type']
        '''if hscboard_type == 'Central-Board':
            hscboard_type==0
        else:
            hscboard_type==1'''
        
        hscstream=request.form['hscboard_type']
        '''if hscstream == 'Arts':
            hscstream == 0
        elif hscstream == 'Commerce':
            hscstream == 1
        else:
            hscstream == 2'''

        degree_p = float(request.form['degree_p'])
        d_type=request.form['d_type']
        '''if d_type == 'Science':
            d_type == 2

        elif d_type == 'Management':
            d_type == 0

        else:
            d_type == 1'''
        
        experience=request.form['experience']
        '''if experience == 'Yes':
            experience = 1
        else:
            experience = 0'''

        etest = float(request.form['etest'])	
        specialization = request.form['specialization']
        '''if specialization == 'Mkt&HR':
            specialization = 1
        else:
            specialization = 0'''

        mba_p = float(request.form['mba_p'])
        
        prediction=model.predict([[ssc_p,board_type,hsc_p,hscboard_type,hscstream,degree_p,d_type,experience,etest,specialization, mba_p]])
        output=(prediction[0])
        if output==1:
            return render_template('index.html',prediction_texts="You are on right path! Keep it up, you have Higher chances of getting placed.")
        else:
            return render_template('index.html',prediction_texts="You need to work hard for getting placed. Currently you have low chances of getting placed.")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)