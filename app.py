import streamlit as st
import pandas as pd
import pickle
import xgboost as xgb
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
columns = pickle.load(open('data/columns_new.pkl', 'rb'))

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
nationality = {
    "Portuguese": 1,
    "German": 2,
    "Spanish": 6,
    "Italian": 11,
    "Dutch": 13,
    "English": 14,
    "Lithuanian": 17,
    "Angolan": 21,
    "Cape Verdean": 22,
    "Guinean": 24,
    "Mozambican": 25,
    "Santomean": 26,
    "Turkish": 32,
    "Brazilian": 41,
    "Romanian": 62,
    "Moldova (Republic of)": 100,
    "Mexican": 101,
    "Ukrainian": 103,
    "Russian": 105,
    "Cuban": 108,
    "Colombian": 109
}
# Long data (simplify and/or onehot encode)
drop_col=["Mothers_qualification", "Fathers_qualification", "Mothers_occupation", "Fathers_occupation"]
col_list = ['Marital_status', 'Application_mode', 'Course', 'Previous_qualification', ]
replace_dict_list = [marital_status, application_mode, simplified_courses, simplified_previous_qualification]
binary_col = ['Displaced', 'Educational_special_needs', 'Debtor', 'Tuition_fees_up_to_date', 
               'Scholarship_holder', 'International']

# Input parameters
user_inputs = {}
st.header("Input Parameters")
col1, col2, col3, col4 = st.columns(4)
with col1:
    Marital_status = st.selectbox("Marital Status", list(marital_status.keys()))
with col2:
    application_mode = st.selectbox("Application Mode", list(application_mode.keys()))
with col3:
    application_order = st.number_input("Application Order", min_value=0, max_value=9, value=4)
with col4:
    Daytime_evening_attendance = st.selectbox("Daytime/Evening Attendance", list(daytime_dict.values()))

col1, col2, col3 = st.columns(3)
with col1:
    course = st.selectbox("Course", list(simplified_courses.keys()))
with col2: 
    Previous_qualification = st.selectbox("Previous Qualification", list(simplified_previous_qualification.keys()))
with col3:    
    nacionality = st.selectbox("National", list(nationality.keys())) 

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    Previous_qualification_grade = st.number_input("Previous Qualification Grade", min_value=0, max_value=400, value=100)
with col2:
    Admission_grade = st.number_input("Admission Grade", min_value=0.0, max_value=400.0, value=100.0, step=0.1)
with col3:
    Displaced = st.selectbox("Displaced", list(binary_dict.values()))
with col4:    
    Educational_special_needs = st.selectbox("Educational Special Needs", list(binary_dict.values()))
with col5:
    Debtor = st.selectbox("Debtor", list(binary_dict.values()))
    
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    Tuition_fees_up_to_date = st.selectbox("Tuition Fees Up to Date", list(binary_dict.values()))
with col2:
    gender = st.selectbox("Gender", list(gender_dict.values()))
with col3:
    Scholarship_holder = st.selectbox("Scholarship Holder", list(binary_dict.values()))
with col4:
    Age_at_enrollment = st.number_input("Age at Enrollment", min_value=16, max_value=100, value=19)
with col5:
    international = st.selectbox("International", list(binary_dict.values()))

col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    Curricular_units_1st_sem_credited = st.number_input("Curricular Units 1st Sem Credited", min_value=0, max_value=100, value=15)
with col2:
    Curricular_units_1st_sem_enrolled = st.number_input("Curricular Units 1st Sem Enrolled", min_value=0, max_value=100, value=18)
with col3:
    Curricular_units_1st_sem_evaluations = st.number_input("Curricular Units 1st Sem Evaluations", min_value=0, max_value=100, value=30)
with col4:
    Curricular_units_1st_sem_approved = st.number_input("Curricular Units 1st Sem Approved", min_value=0, max_value=100, value=15)
with col5:
    Curricular_units_1st_sem_grade = st.number_input("Curricular Units 1st Sem Grade", min_value=0.0, max_value=100.0, value=13.5, step=0.01)
with col6:
    Curricular_units_1st_sem_without_evaluations = st.number_input("Curricular Units 1st Sem Without Evaluations", min_value=0, max_value=100, value=10)

col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    Curricular_units_2nd_sem_credited = st.number_input("Curricular Units 2nd Sem Credited", min_value=0, max_value=100, value=15)
with col2:
    Curricular_units_2nd_sem_enrolled = st.number_input("Curricular Units 2nd Sem Enrolled", min_value=0, max_value=100, value=18)
with col3:
    Curricular_units_2nd_sem_evaluations = st.number_input("Curricular Units 2nd Sem Evaluations", min_value=0, max_value=100, value=30)
with col4:
    Curricular_units_2nd_sem_approved = st.number_input("Curricular Units 2nd Sem Approved", min_value=0, max_value=100, value=15)
with col5:
    Curricular_units_2nd_sem_grade = st.number_input("Curricular Units 2nd Sem Grade", min_value=0.0, max_value=100.0, value=13.5, step=0.01)
with col6:
    Curricular_units_2nd_sem_without_evaluations = st.number_input("Curricular Units 2nd Sem Without Evaluations", min_value=0, max_value=100, value=6)

col1, col2, col3 = st.columns(3)
with col1:
    unemployment_rate = st.number_input("Unemployment Rate", min_value=0.0, max_value=100.0, value=7.6, step=0.1)
with col2:
    inflation_rate = st.number_input("Inflation Rate", min_value=-50.0, max_value=100.0, value=0.0, step=0.1)
with col3:
    gdp = st.number_input("GDP", min_value=-50.0, max_value=100000.0, value=0.0, step=0.1)


user_inputs["Marital_status"] = [Marital_status]
user_inputs["Application_mode"] = [application_mode]
user_inputs["Application_order"] = [application_order]
user_inputs["Course"] = [course]
user_inputs["Daytime_evening_attendance"] = [Daytime_evening_attendance]
user_inputs["Previous_qualification"] = [Previous_qualification]
user_inputs["Previous_qualification_grade"] = [Previous_qualification_grade]
user_inputs["Nacionality"] = [nacionality]
user_inputs["Admission_grade"] = [Admission_grade]
user_inputs["Displaced"] = [Displaced]
user_inputs["Educational_special_needs"] = [Educational_special_needs]
user_inputs["Debtor"] = [Debtor]
user_inputs["Tuition_fees_up_to_date"] = [Tuition_fees_up_to_date]
user_inputs["Gender"] = [gender]
user_inputs["Scholarship_holder"] = [Scholarship_holder]
user_inputs["Age_at_enrollment"] = [Age_at_enrollment]
user_inputs["International"] = [international]
user_inputs["Curricular_units_1st_sem_credited"] = [Curricular_units_1st_sem_credited]
user_inputs["Curricular_units_1st_sem_enrolled"] = [Curricular_units_1st_sem_enrolled]
user_inputs["Curricular_units_1st_sem_evaluations"] = [Curricular_units_1st_sem_evaluations]
user_inputs["Curricular_units_1st_sem_approved"] = [Curricular_units_1st_sem_approved]
user_inputs["Curricular_units_1st_sem_grade"] = [Curricular_units_1st_sem_grade]
user_inputs["Curricular_units_1st_sem_without_evaluations"] = [Curricular_units_1st_sem_without_evaluations]
user_inputs["Curricular_units_2nd_sem_credited"] = [Curricular_units_2nd_sem_credited]
user_inputs["Curricular_units_2nd_sem_enrolled"] = [Curricular_units_2nd_sem_enrolled]
user_inputs["Curricular_units_2nd_sem_evaluations"] = [Curricular_units_2nd_sem_evaluations]
user_inputs["Curricular_units_2nd_sem_approved"] = [Curricular_units_2nd_sem_approved]
user_inputs["Curricular_units_2nd_sem_grade"] = [Curricular_units_2nd_sem_grade]
user_inputs["Curricular_units_2nd_sem_without_evaluations"] = [Curricular_units_2nd_sem_without_evaluations]
user_inputs["Unemployment_rate"] = [unemployment_rate]
user_inputs["Inflation_rate"] = [inflation_rate]
user_inputs["GDP"] = [gdp]

data = pd.DataFrame(user_inputs)
df = pd.DataFrame(columns=columns)

# button
if button := st.button("Predict"):
    # Use the inverted dictionary to map 'Nacionality' column from numbers to names
    data['Nacionality'] = data['Nacionality'].map(nationality)
    data['Nacionality'] = data['Nacionality'].astype('int')                                             
    num_col = data.select_dtypes(include=['int64', 'float64', 'int32']).columns.tolist()
    cat_col = data.select_dtypes(include=['object', 'category']).columns.tolist()                                            
    data[num_col] = scaler.transform(data[num_col])
    data = pd.get_dummies(data, columns=cat_col)
    data_reordered = data.reindex(columns=df.columns, fill_value=1)
    data_reordered.fillna(0, inplace=True)
    # change all the boolean columns to int
    for col in data_reordered.columns:
        if data_reordered[col].dtype == 'bool':
            data_reordered[col] = data_reordered[col].astype(int)
    # Predict
    prediction = model.predict(data_reordered)
    mapping = {'Dropout': 0, 'Enrolled': 1, 'Graduate': 2}
    reversed_mapping = {value: key for key, value in mapping.items()}
    predictions = [reversed_mapping[prediction] for prediction in prediction]
    prediction = predictions[0]
    st.write(f"Predicted Performance:   {prediction}")


