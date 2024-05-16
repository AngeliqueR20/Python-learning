import pickle
import streamlit as st

jantung_model = pickle.load(open('jantung_model.sav'))

st.title('Data Mining Prediksi Jantung')

Age = st.text_input ('input nilai Age')
Sex = st.text_input ('input nilai Sex')
ChestPainType = st.text_input ('input nilai ChestPainType')
RestingBP = st.text_input ('input nilai RestingBP')
Cholesterol = st.text_input ('input nilai Cholesterol')
FastingBS = st.text_input ('input nilai FastingBS')
RestingECG = st.text_input ('input nilai RestingECG')
MaxHR = st.text_input ('input nilai MaxHR')
ExerciseAngina = st.text_input ('input nilai ExerciseAngina')
Oldpeak = st.text_input ('input nilai Oldpeak')
ST_Slope = st.text_input ('input nilai ST_Slope')

jantung_model = pickle.load(open('jantung_model.sav', 'rb'))
