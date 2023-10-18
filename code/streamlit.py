import numpy as np 
import pandas as pd  

import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.title("Data Profiling App")

# Sidebar for user to upload their data
st.sidebar.header("Upload your data")
uploaded_file = st.sidebar.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Read the uploaded data
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
    else:
        st.error("Unsupported file format. Please upload a CSV or Excel file.")
        st.stop()
       
    pr = ProfileReport(df, explorative=True)

    # Display the profiling report in Streamlit
    st.header("Data Profiling Report")
    st_profile_report(pr)


