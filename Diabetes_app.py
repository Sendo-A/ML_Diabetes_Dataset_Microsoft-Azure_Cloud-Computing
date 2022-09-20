import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn
import os
import joblib
from sklearn.model_selection import train_test_split
import azureml.train.automl


st.set_page_config(layout="wide")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Logo_EHTP_ENTREPRISES.jpg/800px-Logo_EHTP_ENTREPRISES.jpg",width=150)   
st.write("""
# MSDE4 : Cloud Computing Project
## Diabetes Prediction App

""")


st.sidebar.image("https://i0.wp.com/pharmaceuticalintelligence.com/wp-content/uploads/2021/05/machine-learning-in-healthcare-1-768x402-1.jpg?ssl=1", width = 300)
with st.sidebar:
        st.write('This app can provide assistance in predicting whether the person will be diabetic or not based on historical data of The client')
        st.write('In order to get the best results the input data must be as accurate as possible')

st.sidebar.header("User Input Parameters")



def user_input_features():
    Pregnancies = st.sidebar.slider("Pregnancies", 0,17,step=1)
    Glucose = st.sidebar.slider("Glucose ", 0,199,step=1)
    Blood_Pressure = st.sidebar.slider("BloodPressure ", 0,122,step=1)
    Skin_Thickness = st.sidebar.slider("SkinThickness ", 0,99,step=1)
    Insulin = st.sidebar.slider("Insulin ", 0,846,step=1)
    BMI = st.sidebar.number_input("BMI ", 0.00,68.5,step=0.01)
    Diabetes_Pedigree_Function = st.sidebar.number_input("DiabetesPedigreeFunction ", 0.00 ,3.5,step=0.01)
    Age = st.sidebar.slider("Age ", 21,81,step=1)   

    data = {"Pregnancies": Pregnancies,
            "Glucose": Glucose,
            "BloodPressure":Blood_Pressure,
            "SkinThickness": Skin_Thickness,
            "Insulin": Insulin,
            "BMI": BMI,
            "DiabetesPedigreeFunction": Diabetes_Pedigree_Function,
            "Age": Age,}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader("User Input parameters")
st.write(df)


model=joblib.load(open("model.pkl","rb"))
prediction = model.predict(df)

st.subheader('Class labels and their corresponding index number')
st.write(pd.DataFrame(model.classes_))
prediction_proba = model.predict_proba(df)

st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)

if st.button("Predict"):

    model=joblib.load(open("model.pkl","rb"))
    prediction = model.predict(df)
    if prediction[0] == 1:
        st.write('Positive  With {} % Chance Of Getting diabetic'.format(round(prediction_proba[0][1]*100 , 2)))
    elif prediction[0] == 0:
        st.write('Negative With {}  % Chance Of Not Getting diabetic'.format(round(prediction_proba[0][0]*100 , 2)))
