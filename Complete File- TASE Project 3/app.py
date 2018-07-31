from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home0.html')

@app.route('/getdefault',methods=['POST','GET'])
def get_default():
    if request.method=='POST':
        result=request.form
		
		#Prepare the feature vector for prediction

        pkl_file = open('cat', 'rb')
        index_dict = pickle.load(pkl_file)
        new_vector = np.zeros(len(index_dict))

        try:
            new_vector[index_dict['LIMIT_BAL'+str(result['limit_bal'])]] = 1
        except:
            pass
        try:
            new_vector[index_dict['SEX'+str(result['sex'])]] = 1
        except:
            pass
        try:
            new_vector[index_dict['EDUCATION'+str(result['education'])]] = 1
        except:
            pass
        try:
            new_vector[index_dict['MARRIAGE'+str(result['marriage'])]] = 1
        except:
            pass
        try:
            new_vector[index_dict['AGE'+str(result['age'])]] = 1
        except:
            pass
        try:
            new_vector[index_dict['BILL_AMT1'+str(result['bill_amt1'])]] = 1
        except:
            pass
        try:
            new_vector[index_dict['PAY_AMT1'+str(result['bill_amt1'])]] = 1
        except:
            pass
        
      
        pkl_file = open('tasemodel.pkl', 'rb')
        logmodel = pickle.load(pkl_file)
        prediction = logmodel.predict([new_vector])
        
        return render_template('result.html',prediction=prediction)

    
if __name__ == '__main__':
	app.run()

