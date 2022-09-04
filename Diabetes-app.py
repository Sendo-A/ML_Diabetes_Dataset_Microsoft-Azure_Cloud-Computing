import streamlit as st
import pandas as pd
import numpy as np
import pickle


st.set_page_config(layout="wide")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Logo_EHTP_ENTREPRISES.jpg/800px-Logo_EHTP_ENTREPRISES.jpg",width=150)   
st.write("""
# MSDE4 : Cloud Computing Project
## Diabetes Prediction App

""")


#st.sidebar.image("https://github.com/kamruleee51/Diabetes-Prediction-Using-ML-Classifiers", width = 500)
with st.sidebar:
        st.write('This app can provide assistance in predicting whether the person will be diabetic or not based on historical data of The client')
        st.write('In order to get the best results the input data must be as accurate as possible')

st.sidebar.header("User Input Parameters")



def user_input_features():
    Pregnancies = st.sidebar.slider("Pregnancies", 0,17,step=1)
    Glucose = st.sidebar.slider("Glucose ", 0,199,step=1)
    Blood_Pressure = st.slider("Blood Pressure ", 0,122,step=1)
    Skin_Thickness = st.slider("Skin Thickness ", 0,99,step=1)
    Insulin = st.slider("Insulin ", 0,846,step=1)
    BMI = st.number_input("BMI ", 0.00,68.5,step=0.01)
    Diabetes_Pedigree_Function = st.number_input("Diabetes Pedigree Function ", 0.00 ,3.5,step=0.01)
    Age = st.slider("Age ", 21,81,step=1)   

    data = {"Pregnancies": Pregnancies,
            "Glucose": Glucose,
            "Blood Pressure":Blood_Pressure,
            "Skin Thickness": Skin_Thickness,
            "Insulin": Insulin,
            "BMI": BMI,
            "Diabetes Pedigree Function": Diabetes_Pedigree_Function,
            "Age": Age,}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader("User Input parameters")
st.write(df)

VE_model=pickle.load(open("C:/Users/Eagle Road/Desktop/EHTP/Data engineering/Cloud computing/Q7/MODEL PKL/voting-ensemble_model.pkl","rb"))
prediction = VE_model.predict(df)


st.subheader('Class labels and their corresponding index number')
st.write(pd.DataFrame(VE_model.classes_))
prediction_proba = VE_model.predict_proba(df)

st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)


if st.button("Predict"):

    VE_model=pickle.load(open("C:/Users/Eagle Road/Desktop/EHTP/Data engineering/Cloud computing/Q7/MODEL PKL/voting-ensemble_model.pkl", "rb"))
    prediction = VE_model.predict(df)
    if prediction[0] == 1:
        st.write('Positive  With {} % Chance Of Being Diabetic'.format(round(prediction_proba[0][1]*100 , 2)))
    elif prediction[0] == 0:
        st.write('Negative With {}  % Chance Of Not Diabetic'.format(round(prediction_proba[0][0]*100 , 2)))