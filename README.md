# Home-Credit Default Risk using Deep Learning

http://default-risk.herokuapp.com

## Overview
Many people struggle to get loans due to insufficient or non-existent credit histories. And, unfortunately, this population is often taken advantage of by untrustworthy lenders. Companies like Home Credit strives to broaden financial inclusion for the unbanked population by providing a positive and safe borrowing experience. In order to make sure this underserved population has a positive loan experience, Home Credit makes use of a variety of alternative data (e.g., including telco and transactional information) to predict their clients' repayment abilities. By using various Statistical, Machine Learning  and Deep learning methods we unlock the full potential of their data. Doing so will ensure that clients capable of repayment are not rejected and that loans are given with a principal, maturity, and repayment calendar that will empower their clients to be successful. 

The objective of this project is to use historical loan application data to predict whether or not an applicant will be able to repay a loan. This is a standard supervised classification task:

- Supervised: The labels are included in the training data and the goal is to train a model to learn to predict the labels from the features

- Classification: The label is a binary variable, 0 (will repay loan on time), 1 (will have difficulty repaying loan)

In this project, the goals achieved are :
- Data Exploration routines are designed and implemented to do Statistical analysis and Visualization.
- Classification models such as Naïve Bayes, Logistic Regression, Support Vector machine (SVM), Decision Tree, Random Forest, Gradient Boosting Machine (GBM) and Deep Learning are built to predict whether or not an applicant will be able to repay a loan. 
- Evaluated Classification models by Accuracy, Confusion Matrix, Precision, Recall, True Negative Rate (TNR), False Discovery Rate (FDR), Gain Chart, Lift Chart, K-S Chart, ROC – AUC chart.
- Deployed the Final solution as a Web application (Restful API).

## Data Sources
The data is provided by Home Credit, a service dedicated to provided lines of credit (loans) to the unbanked population. Predicting whether or not a client will repay a loan or have difficulty is a critical business need, and Home Credit wants to unlock the full potential of their data to see what sort of machine learning/deep learning models can be develop to help them in this task.

## Data Exploration
Data Exploration is an open-ended process where we calculate statistics and make figures to find trends, anomalies, patterns, or relationships within the data. The goal of Data Exploration is to learn what our data can tell us. It generally starts out with a high level overview, then narrows in to specific areas as we find intriguing areas of the data. The findings may be interesting in their own right, or they can be used to inform our modeling choices, such as by helping us decide which features to use.

We use Label Encoding for any categorical variables with only 2 categories and One-Hot Encoding for any categorical variables with more than 2 categories.

### Most Valuable Plot (MVP) – Combination Charts
We do statistical analysis and visualization for both numeric and categorical variables. We generate descriptive statistics that summarize the central tendency, dispersion and shape of a data’s distribution. 

For numeric variables, we plot histograms to show the distribution of the numerical variable with one y-axis which is for count of the values in the numeric variable and also plot line graph with another y-axis which for the percent of Target=1 (will have difficulty repaying loan).

For categorical variables, we plot bar chart to show the distribution of the categorical variable and sort in decreasing order with one y-axis which is for count of the values for the categories and also plot line graph with another y-axis which for the percent of Target=1 (will have difficulty repaying loan). 

This plot is called the Most Valuable Plot (MVP), also called Combination Chart. The combination chart is the best visualization method to demonstrate the predictability power of a predictor (X-axis) against a target (Y-axis). They show us how the variable affecting the percent of Target=1, thereby demonstrate the predictability power of a variable for our predictive modeling. From the visual, we can say that as the count of the variable is increasing/decreasing, the percent of Target=1 is decreasing or increasing depending on the steepness of the line, so the loan are repaid more or less depending the percent decrease or increase respectively.

## Data Modeling 
We use the following Machine learning algorithms and built Classification models for our supervised classification task.
### 1)	Naïve Bayes
### 2)	Logistic Regression
### 3)	Decision Tree
### 4)	Random Forest
### 5)	Gradient Boosting Machine (GBM)
### 6)	Deep Learning

Out of the above, the first four are Baseline models and last three are improved models.

## Model Evaluation 

Evaluated Classification models by Accuracy, Confusion Matrix, Precision, Recall, True Negative Rate (TNR), False Discovery Rate (FDR), Gain Chart, Lift Chart, K-S Chart, ROC – AUC chart.

After comparing the performance of above technique Gradient Boosting machine(GBM) performs the best followed by the Deep Learning neural network classifier followed by Random Forest.

## RESTful API with Python and Flask
A RESTful API is an application program interface (API) that uses HTTP requests to GET, PUT, POST and DELETE data. 

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. It is relatively easy to set up a website on Flask using Jinja2 templating. 

Heroku is a cloud platform as a service (PaaS) supporting several programming languages.

## Python -> Machine Learning/Deep Learning Model -> pickle model -> flask -> deploy on Heroku

We save the model to disk using Python’s built in persistence model (pickle or dill) and use this model for prediction on new data.

Now we create the simple flask app. The flask app consists of 2 main components: the python app (app.py) and the HTML templates. While we can return HTML code from the python file itself, it would be cumbersome to code entire HTML as a string in the python file. Templating come to the rescue!

The Final Machine Learning Model is deployed as a Web application (Restful API) on Heroku Cloud platform, link for demo : http://default-risk.herokuapp.com


More Information is in the Home_Credit_report.pdf.
