import streamlit as st
import pandas as pd
import joblib

pkl = joblib.load("model/bullying_model.pkl")

st.title('¿Eres víctima de bullying?')

st.write( 'Responde a las siguientes preguntas para definir si usted está siendo víctima del Bullying')


edad = st.slider('¿Cuál es tu edad?', 11, 18)
sexo = st.radio('¿Cuál es tu sexo?', ["Hombre", "Mujer"], index=None, key=0)
agresion = st.radio('¿Te han atacado físicamente en algún momento?', ["Sí", "No"], index=None, key=1)
peleas = st.radio('¿Has participado en peleas físicas en algún momento?', ["Sí", "No"], index=None, key=2)
frecuenciaSoledad = st.selectbox(
    '¿Con qué frecuencia te sientes solo(a)?',
    ('Nunca', 'Raramente', 'A veces','La mayor parte del tiempo','Siempre'))
amigos = st.selectbox(
    '¿Cuántos amigos cercanos tienes?',
    (0,1,2,3))
asistencia = st.radio('¿Te has ausentado de la escuela sin permiso en los últimos 12 meses?', ["Sí", "No"], index=None, key=3)

amabilidad = st.selectbox(
    '¿Consideras que otros estudiantes son amables y serviciales contigo?',
    ('Nunca', 'Raramente', 'A veces','La mayor parte del tiempo','Siempre'))
padres = st.selectbox(
    '¿Sientes que tus padres comprenden tus problemas?',
    ('Nunca', 'Raramente', 'A veces','La mayor parte del tiempo','Siempre'))
soledad = st.radio('¿Te has sentido solo(a) la mayor parte del tiempo o siempre en los últimos 12 meses?', ["Sí", "No"], index=None, key=4)
clases = st.radio('¿Has faltado a clases o a la escuela sin permiso en los últimos 12 meses?', ["Sí", "No"], index=None, key=5)
subpeso = st.radio('¿Has experimentado subpeso en algún momento?', ["Sí", "No"], index=None, key=6)
sobrepeso = st.radio('¿Has experimentado sobrepeso en algún momento?', ["Sí", "No"], index=None, key=7)
obesidad = st.radio('¿Has experimentado obesidad en algún momento?', ["Sí", "No"], index=None, key=8)

if st.button('Enviar'):

    data =pd.DataFrame([[edad, sexo, agresion, peleas, frecuenciaSoledad, amigos,asistencia, amabilidad, padres, soledad,clases,subpeso, sobrepeso, obesidad]], 
                        columns=['Custom_Age', 'Sex', 'Physically_attacked', 'Physical_fighting', 'Felt_lonely', 'Close_friends', 'Miss_school_no_permission', 'Other_students_kind_and_helpful', 'Parents_understand_problems', 'Most_of_the_time_or_always_felt_lonely','Missed_classes_or_school_without_permission','Were_underweight','Were_overweight','Were_obese'])
    data = data.replace(["Hombre", "Mujer"], [1, 0])
    data = data.replace(["Sí", "No"], [1, 0])
    data = data.replace({'Nunca':1, 'Raramente':2, 'A veces':3,'La mayor parte del tiempo':4,'Siempre':5})
    prediccion = pkl.predict(data)[0]
    st.write(prediccion)

