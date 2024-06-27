import streamlit as st
import pandas as pd
import pickle
import xgboost as xgb
from sklearn.preprocessing import OneHotEncoder
import plotly.express as px

st.set_page_config(
    page_title="Predicting Student Performance",
    page_icon="📚",
)
st.write("# Predicting Student Performance")

# Load the model
model = pickle.load(open('model/model.pkl', 'rb'))
encoder = pickle.load(open('model/encoder.pkl', 'rb'))
scaler = pickle.load(open('model/scaler.pkl', 'rb'))
columns = pickle.load(open('data/columns.pkl', 'rb'))

# Category description
binary_dict = {0: 'No', 1: 'Yes'}
gender_dict = {1: 'male', 0: 'female'}
daytime_dict = {1: 'Daytime', 0: 'Evening'}

marital_status = {
    "Single": [1],
    "Married": [2],
    "Windower": [3],
    "Divorced": [4],
    "Facto Union": [5],
    "Separated": [6]

}
application_mode = {
    "General Contingent": [1, 17, 18],
    "Special Contingents": [2, 5, 10, 16, 26, 27],
    "International Students": [15, 57],
    "Holders of Other Qualifications": [7, 39, 44, 53],
    "Transfers and Changes": [42, 43, 51]
}
simplified_courses = {
    "Biofuel Technologies": [33],
    "Animation & Multimedia": [171],
    "Social Service": [8014, 9238],
    "Agronomy": [9003],
    "Communication Design": [9070],
    "Veterinary Nursing": [9085],
    "Informatics Engineering": [9119],
    "Equine Studies": [9130],
    "Management": [9147, 9991],
    "Tourism": [9254],
    "Nursing": [9500],
    "Oral Hygiene": [9556],
    "Advertising & Marketing": [9670],
    "Journalism & Communication": [9773],
    "Basic Education": [9853]
}
simplified_previous_qualification = {
    "Secondary": [1, 9, 10, 12, 14, 15],
    "Bachelor's": [2, 3, 40],
    "Master's": [4, 43],
    "Doctorate": [5],
    "Frequent Higher Education": [6],
    "Basic Education": [19, 38],
    "Tech Specialization": [39],
    "Professional Higher Tech": [42]
}

# Long data (simplify and/or onehot encode)
drop_col=["Mothers_qualification", "Fathers_qualification", "Mothers_occupation", "Fathers_occupation"]
col_list = ['Marital_status', 'Application_mode', 'Course', 'Previous_qualification', ]
replace_dict_list = [marital_status, application_mode, simplified_courses, simplified_previous_qualification]
binary_col = ['Displaced', 'Educational_special_needs', 'Debtor', 'Tuition_fees_up_to_date', 
               'Scholarship_holder', 'International']

# upload file
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

def replace_values(df, column, replace_dict):
    for key, values in replace_dict.items():
        for value in values:
            df.loc[df[column] == value, column] = key
    return df

# if file is uploaded
if uploaded_file is not None:
    # Read the file
    df = pd.read_csv(uploaded_file, sep=';')
    # df = df_ori.copy()
    # df_ori.drop(columns=['Status'], inplace=True)
    # Drop columns
    df.drop(drop_col, axis=1, inplace=True)
    # Use only selected columns
    # Replace values
    ## binary columns
    for col in binary_col:
        df[col] = df[col].map(binary_dict)
        df[col] = df[col].astype('category')
        
    ## gender & attendance
    df['Daytime_evening_attendance'] = df['Daytime_evening_attendance'].map(daytime_dict)
    df['Daytime_evening_attendance'] = df['Daytime_evening_attendance'].astype('category')
    df['Gender'] = df['Gender'].map(gender_dict)
    df['Gender'] = df['Gender'].astype('category')

    ## num to cat
    for col, replace_dict in zip(col_list, replace_dict_list):
        print(f'Processing {col}')
        df = replace_values(df, col, replace_dict)
        df[col] = df[col].astype('category')
        
    ## status(label)
    df['Status'] = df['Status'].astype('category')
    # df = df[columns]
    # st.write(df.head())
    df.drop(columns=['Status'], inplace=True)
    df_ori = df.copy()

    num_col = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    cat_col = df.select_dtypes(include=['object', 'category']).columns.tolist()  # Adjusted to include 'object' dtype for non-encoded categorical data
    # Scale the numerical variables
    df[num_col] = scaler.transform(df[num_col])
    # One-hot encode the categorical variables onehotencoder
    df = pd.get_dummies(df, columns=cat_col)
    # Make predictions
    predictions = model.predict(df)
    # Define the mapping
    mapping = {'Dropout': 0, 'Enrolled': 1, 'Graduate': 2}
    # Map the predictions
    reversed_mapping = {value: key for key, value in mapping.items()}
    predictions = [reversed_mapping[prediction] for prediction in predictions]
    # add the prediction to the first col of dataframe
    df_ori.insert(0, 'Status', predictions)
    # streamlit plotly pie chart for prediction
    st.write("### Prediction Distribution")
    fig = px.pie(df_ori, names='Status', hole=.3)
    st.plotly_chart(fig)
    
    st.write("### Predictions")
    st.write(df_ori)
    
    # Download the predictions
    csv = df_ori.to_csv(index=False)
    st.download_button(
        label="Download Predictions",
        data=csv,
        file_name='predictions.csv',
        mime='text/csv',
    )
    

    
        

