import streamlit as st
import pickle
import numpy as np 
import xgboost

model = pickle.load(open(r'C:\Users\ajayk\Downloads\CALORIES_BURNT-20231015T155831Z-001\CALORIES_BURNT\Model\model.pkl', 'rb'))
gender = [0,1]
#Accepting the input from user and prediction
st.title('Number of Calories Burnt Prediction')
Gender = st.selectbox('Select your gender (0-male, 1-female)',sorted(gender))
col1,col2 = st.columns(2)
with col1:
    Age = st.number_input('Age')
with col2:
    Height = st.number_input('Height')

col3,col4,col5 = st.columns(3)

with col3:
    Duration = st.number_input('Exercise Duration (in mins)')
with col4:
    Heart_Rate = st.number_input('Heart Rate')
with col5:
    Body_Temp = st.number_input('BOdy Temp (in Celsius)')

if st.button('Predict Calories Burnt'):

    input_df = np.array([Gender,Age,Height,Duration,Heart_Rate,Body_Temp])
    input_df = input_df.reshape(1,-1)
    result = model.predict(input_df)
    st.header("Calories burnt - " + str(int(result[0])))