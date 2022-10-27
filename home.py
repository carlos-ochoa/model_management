import pandas as pd
import streamlit as st
import requests
import os

server = os.environ["MLFLOW_TRACKING_SERVER"]

st.title("Spotlight Model Management")

models = requests.get("{server}/2.0/preview/mlflow/registered-models/list")

st.write(models)

models_df = pd.DataFrame(models)
st.dataframe(models_df)

model_details = st.text_input("Model to check","")