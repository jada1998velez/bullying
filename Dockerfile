FROM python:3.8
RUN pip install streamlit joblib pandas scikit-learn==1.2.2
COPY src/* /app/
COPY model/bullying_model.pkl /app/model/bullying_model.pkl

WORKDIR /app
ENTRYPOINT [ "streamlit", "run", "joblib" "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
