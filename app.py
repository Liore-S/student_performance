import streamlit as st
import pandas as pd
import pickle
import xgboost as xgb

st.set_page_config(
    page_title="Predicting Student Performance",
    page_icon="📚",
)

# Load the model
model = pickle.load(open('model/model.pkl', 'rb'))
encoder = pickle.load(open('model/encoder.pkl', 'rb'))
scaler = pickle.load(open('model/scaler.pkl', 'rb'))

# upload file
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")


