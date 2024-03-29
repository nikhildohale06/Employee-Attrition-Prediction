import numpy as np
import pandas as pd
import pickle
import streamlit as st

with open('model.pickle','rb') as pkl:
    classifier = pickle.load(pkl)

df = pd.read_csv(r"C:\Users\Nikhil\ML Projects\Employee-Attrition.csv")
df.head()

def main():
    st.title("Employee Attrtion Prediction")
    col1,col2 = st.columns(2)

    with col1:
        Age = st.number_input('Age')
        Education = st.number_input('Education')
        EducationField = st.number_input('EducationField')
        Gender = st.number_input('Gender')
        MaritalStatus = st.number_input('MaritalStatus')
        EnvironmentSatisfaction = st.number_input('EnvironmentSatisfaction')
        JobInvolvement = st.number_input('JobInvolvement')
        MonthlyIncome = st.number_input('MonthlyIncome')
        Over18 = st.number_input('Over18')
        
    with col2:
        RelationshipSatisfaction = st.number_input('RelationshipSatisfaction')
        JobSatisfaction = st.number_input('JobSatisfaction')
        WorkLifeBalance = st.number_input('WorkLifeBalance')
        Department = st.number_input('Department')
        BusinessTravel = st.number_input('BusinessTravel')
        JobLevel = st.number_input('JobLevel')
        JobRole = st.number_input('JobRole')
        OverTime = st.number_input('OverTime')
        PerformanceRating = st.number_input('PerformanceRating')

    if st.button('Predict'):
        res = classifier.predict([[Age,BusinessTravel,Department,Education,EducationField,EnvironmentSatisfaction,Gender,JobInvolvement,JobLevel,JobRole,JobSatisfaction,MaritalStatus,MonthlyIncome,Over18,OverTime,PerformanceRating,RelationshipSatisfaction,WorkLifeBalance]])
        if (res[0]==0):
            st.success("Employee will continue with company")
        else:
            st.success('Employee will Attrite')
       

if __name__ =='__main__':
    main()    




