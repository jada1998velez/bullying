FROM python:3.8
RUN pip install streamlit joblib pandas 
COPY src/* /app/
# COPY model/bullying_model.pkl /app/model/bullying_model.pkl

WORKDIR /app
ENTRYPOINT [ "streamlit", "run", "app.py"]
