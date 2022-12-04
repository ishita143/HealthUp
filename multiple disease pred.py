# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 19:22:01 2022

@author: admin
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

diabetes_model = pickle.load(open('C:/Users/admin/Desktop/multiple disease prediction system/saved model/Diabetes_disease_data.sav', 'rb'))

heart_model = pickle.load(open('C:/Users/admin/Desktop/multiple disease prediction system/saved model/heart_disease_data.sav', 'rb'))

parkinsons_model = pickle.load(open('C:/Users/admin/Desktop/multiple disease prediction system/saved model/parkinsons_model.sav', 'rb'))

# navigation or side bar
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System', 
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction', 
                            'Parkinsons Prediction'],
                           
                           icons = ['activity', 'heart', 'person'],
                          
                           default_index = 0)


# prediction page
if (selected == 'Diabetes Prediction'):
    
    st.title('Diabetes Prediction using ML')
    
    # getting the input data from the user
    # columns for input data
    col1, col2, col3 = st.columns(3)
    
    with col1:    
        Pregnancies = st.text_input('Number of pregnencies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin value')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the person')
        
    # code for prediction
    diab_diagnosis = ''
    
    # prediction button 
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict(np.array([[float(Pregnancies), float(Glucose), float(BloodPressure), 
                                                   float(SkinThickness), float(Insulin), float(BMI),
                                                   float(DiabetesPedigreeFunction), float(Age)]]))
    
        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is Diabetic'
            
        else:
            diab_diagnosis = 'The person is Not Diabetic'
    
    st.success(diab_diagnosis)
    
    
    
    
    
    
    
if (selected == 'Heart Disease Prediction'):
    
    st.title('Heart Disease Prediction using ML')
    
    age = st.text_input('Age of the person')

    sex = st.text_input('Gender of the person(1 = male 0 = female 2 = trans.)')

    cp = st.text_input('Chest Pain type(1 = typical angina, 2 = atypical angina, 3 = non - anginal pain, 4 = asymptotic)')

    trtbps = st.text_input('Resting Blood Pressure of the person')

    chol = st.text_input('Serum Cholestrol level of preson')

    fbs = st.text_input('6.	Fasting Blood Sugar(If fasting blood sugar > 120mg/dl then : 1 (true) else : 0 (false))')

    restecg = st.text_input('Resting ECG : 0 = normal, 1 = having ST-T wave abnormality, 2 = left ventricular hyperthrophy')

    thalachh = st.text_input('Max heart rate achieved')

    exng = st.text_input('Exercise induced angina : 1 = yes 0 = no')

    oldpeak = st.text_input('Peak exercise ST segment : 1 = upsloping, 2 = flat, 3 = down sloping')

    slp = st.text_input('ST depression induced by exercise relative to rest')

    caa = st.text_input('Number of major vessels (0-3) colored by fluoroscopy')

    thall = st.text_input ('thalassemia : 3 = normal, 6 = fixed defect, 7 = reversable defect')
    
    # code for prediction
    heart_diagnosis = ''
    
    # prediction button 
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict(np.array([[float(age), float(sex), float(cp), float(trtbps), float(chol), float(fbs), float(restecg), float(thalachh),
                                                          float(exng), float(oldpeak), float(slp), float(caa), float(thall)]]))
    
        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person has a Heart Disease'
            
        else:
            heart_diagnosis = 'The person does Not have a Heart Disease'
    
    st.success(heart_diagnosis)
    
    
    
if (selected == 'Parkinsons Prediction'):
    
    st.title('Parkinsons Disease Prediction using ML')
    
    
    # columns
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        Fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        Fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        Flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percentage = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_abs = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP:RAP')
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    with col3:
        DDP = st.text_input('Jitter:DDP')
    with col4:
        shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        APQ = st.text_input('MDVP:APQ')
    with col4:
        DDA = st.text_input('Shimmer:DDA')
    with col5: 
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')
    
    
    # code for prediction
    parkinsons_diagnosis = ''
    
    # prediction button 
    
    if st.button('Parkinsons Disease Test Result'):
    
        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = 'The person has Parkinsons Disease'
            
        else:
            parkinsons_diagnosis = 'The person does Not have Parkinsons Disease'
    
    st.success(parkinsons_diagnosis)
    
    
    
    
    
    

    
    
    