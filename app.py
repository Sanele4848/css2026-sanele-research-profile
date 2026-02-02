import streamlit as st

st.set_page_config(page_title="Sanele Mabuza | Research Profile", layout="wide")

with st.sidebar:
    st.title("Sanele Mabuza")
    st.write("Research profile (CSS 2026)")
    st.markdown("---")
    st.write("South Africa")
    st.write("smabuza782@gmail.com")
    st.write("[LinkedIn](https://www.linkedin.com/in/sanele-mabuza-a04742225/)")

st.title("Research Profile")

st.subheader("About me")
st.write("""
I am interested in machine learning and how it can be used to solve real problems using data.
I enjoy building models, testing them properly, and putting them into simple apps that people can use.
My current focus is learning more and preparing for postgraduate study.
""")

st.divider()

st.subheader("Background")
st.write("""
I completed a Bachelor of Information and Communication Technology (BICT) at the University of Mpumalanga (2025).
My final year work focused on Artificial Intelligence Applications (Machine Learning).
""")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Research focus")
    st.write("""
- Machine learning for prediction problems
- Working with real datasets and data cleaning
- Model comparison and model selection
- Turning ML work into simple tools (Streamlit)
""")

with col2:
    st.subheader("Methods I use")
    st.write("""
- Data cleaning and basic feature preparation
- Training and testing multiple models
- Ensemble learning (tree-based models)
- Checking results and improving performance
""")

st.divider()

st.header("Featured work")

st.subheader("Flight Delay Predictor (Machine Learning project)")
st.write("Project mark: 90%")
st.write("""
This project predicts flight delay rates from historical flight data.
I compared multiple models and selected the best one based on results.
""")

st.markdown("**Quick summary**")
st.write("""
- Dataset: over 130000 records
- Approach: ensemble learning
- Best model: Random Forest
""")

st.markdown("**What I did**")
st.write("""
- Cleaned the dataset and handled missing values
- Prepared features and trained multiple models
- Selected Random Forest based on performance
- Built a Streamlit app to test predictions
""")

st.divider()

st.header("What I want to research next")
st.write("""
I want to grow this work further in postgraduate studies.
My long-term interest is applying data science to South African industries, especially mining.
I am interested in safety, monitoring, and early warning systems using data and AI.
""")
