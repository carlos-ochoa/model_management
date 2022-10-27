import pandas as pd
import streamlit as st
import requests
from requests.auth import HTTPBasicAuth
import os

server = os.environ["MLFLOW_TRACKING_SERVER"]

st.title("Spotlight Model Management")

st.write(server)

auth = HTTPBasicAuth(os.environ["MLFLOW_TRACKING_USERNAME"], os.environ["MLFLOW_TRACKING_PASSWORD"])

models = requests.get("{server}/api/2.0/preview/mlflow/registered-models/list", auth = auth)

st.write(models)

models_df = pd.DataFrame(models)
st.dataframe(models_df)

model_details = st.text_input("Model to check","")