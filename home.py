import pandas as pd
import streamlit as st
import requests
from requests.auth import HTTPBasicAuth
import os

server = os.environ["MLFLOW_TRACKING_SERVER"]
user = os.environ["MLFLOW_TRACKING_USERNAME"]
password = os.environ["MLFLOW_TRACKING_PASSWORD"]

st.title("Spotlight Model Management")

st.write(server)
st.write(user)
st.write(password)

auth = HTTPBasicAuth(user, password)

if st.button("Click"):
    models = requests.get(f"{server}/api/2.0/preview/mlflow/registered-models/list", auth = auth)

    st.write(models)

    models_df = pd.DataFrame(models)
    st.dataframe(models_df)

    model_details = st.text_input("Model to check","")