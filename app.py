from flask import Flask, jsonify, request
#import utils.PreProcessing
import pandas as pd
import numpy as np
import sklearn
from flask import Flask, request, render_template
import dill as pickle

app = Flask(__name__)

#@app.route('/predict', methods=['POST'])

@app.route('/')
def home():
	return render_template('home.html')

def color_negative_red(value):
  """
  Colors elements in a dateframe
  green if positive and red if
  negative. Does not color NaN
  values.
  """

  if value ==1:
    color = 'red'
  else:
    color = 'black'

  return 'color: %s' % color

def zero_to_Yes(val):
    if val==0:
       return 'Yes'
    else:
       return 'No'


@app.route('/predict',methods=['POST','GET'])
def upload_route_summary():
    if request.method == 'POST':
       result = request.files['file']
       result = pd.read_csv(result)
       loan_ids = result['SK_ID_CURR']
    
    #app_train = pd.read_csv('/Users/jayborkar/Downloads/all/application_train.csv')
    
    clf = 'model.pk' 
    print("Loading the model...")  
       
    with open(clf,'rb') as f:
              loaded_model = pickle.load(f)
    
    #Sprint("The model has been loaded...doing predictions now...")
    prediction = loaded_model.predict(result)
    prediction_series = list(pd.Series(prediction))
    print("The model has been loaded...doing predictions now...")
    final_predictions = pd.DataFrame(list(zip(loan_ids, prediction_series)))
    final_predictions.columns = ['Loan ID', 'Prediction']
    final_predictions.style.applymap(color_negative_red, subset=['Prediction'])
    final_predictions['Prediction'] = final_predictions['Prediction'].apply(zero_to_Yes)
    #pred = final_predictions[final_predictions.Prediction== 'No']
        
    return render_template('result.html',tables=[final_predictions.to_html(classes='mystyle')],titles = final_predictions.columns.values)
    #return render_template('view1.html')
    #return view1.html.render()titles=final_predictions.columns.values)
    #,pred.to_html(classes='mystyle')


'''
@app.route('/getdelay',methods=['POST','GET'])
def get_delay():
#def apicall():
	"""API Call
	
	Pandas dataframe (sent as a payload) from API Call
	"""
	if request.method=='POST':
	    test_json=request.form()
	    test = pd.read_csv(test_json)
	    loan_ids = test['SK_ID_CURR']

	     #except Exception as e:
		#         raise e
	
	clf = 'model.pk'
	
	if test.empty:
		return(bad_request())
	else:
		#Load the saved model
		print("Loading the model...")
		loaded_model = None
		with open('/Users/jayborkar/Desktop/Python3/'+clf,'rb') as f:
			loaded_model = pickle.load(f)

		print("The model has been loaded...doing predictions now...")
		prediction = loaded_model.predict(test)
		
		"""Add the predictions as Series to a new pandas dataframe
								OR
		   Depending on the use-case, the entire test data appended with the new files
		"""
		#prediction_series = list(pd.Series(predictions))

		#final_predictions = pd.DataFrame(list(zip(loan_ids, prediction_series)))
		
		"""We can be as creative in sending the responses.
		   But we need to send the response codes as well.
		"""
		#responses = jsonify(predictions=final_predictions.to_json(orient="records"))
		#responses.status_code = 200
	
		return render_template('result.html',prediction=prediction)

		#return (responses)
'''

@app.errorhandler(400)
def bad_request(error=None):
	message = {
			'status': 400,
			'message': 'Bad Request: ' + request.url + '--> Please check your data payload...',
	}
	resp = jsonify(message)
	resp.status_code = 400

	return resp
	
if __name__ == '__main__':
	app.debug = True
	app.run()
     
