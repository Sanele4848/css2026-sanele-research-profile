import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sanele Mabuza | Research Profile", layout="wide")

with st.sidebar:
    st.title("Sanele Mabuza")
    st.write("Aspiring Researcher")
    st.markdown("---")
    st.write("smabuza782@gmail.com")
    st.write("Pietermaritzburg, South Africa")
    st.write("[LinkedIn](https://www.linkedin.com/in/sanele-mabuza-a04742225/)")

st.title("Research Profile")

st.markdown("### About")

st.write("""
I apply machine learning to operational prediction problems using historical data. My approach emphasizes 
systematic model comparison (testing multiple algorithms rather than choosing one upfront), proper validation 
that prevents overfitting, and building deployable systems rather than stopping at model training.

My undergraduate work focused on aviation delay prediction using ensemble methods. I am now transitioning 
to postgraduate research in mining applications of machine learning, where I plan to apply similar 
methodological rigor to mining-specific forecasting and optimization problems.
""")

st.markdown("---")

st.markdown("### Background")

col1, col2 = st.columns(2)

with col1:
    st.write("""
    **Education**
    
    Bachelor of Information and Communication Technology  
    University of Mpumalanga, 2025
    
    Focus: Artificial Intelligence Applications (BICT332)
    """)

with col2:
    st.write("""
    **Technical Skills**
    
    Python (scikit-learn, pandas, numpy)  
    Model evaluation and selection  
    Feature engineering  
    Streamlit deployment
    """)

st.markdown("---")

st.markdown("### Undergraduate Research: Flight Delay Prediction")

st.write("""
For my final year undergraduate project, I built a machine learning system to predict flight delay 
rates using 10 years of U.S. airline data (132,695 observations covering 51.4 million flights across 
21 carriers and 389 airports).
""")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Test MAE", "2.12 pp")
col2.metric("R² Score", "0.889")
col3.metric("Best Model", "Random Forest")
col4.metric("Features", "36 engineered")

st.markdown("**Methodology**")

st.write("""
**Data Preprocessing**: Excluded COVID years (2020-2021) to avoid anomalous patterns. Used temporal 
train-test split (2013-2018 train, 2019 validation, 2022-2023 test) to prevent data leakage. Applied 
log transformations to skewed variables and capped extreme outliers at 99th percentile.

**Feature Engineering**: Created 36 features including cyclical time encodings, historical performance 
metrics, operational stress indicators, and delay cause breakdowns. Top 3 features accounted for 92% 
of model importance: seasonal_delay_rate (40%), arr_flights_log (31%), arr_del15_log (20%).

**Model Comparison**: Tested six algorithms (Ridge Regression, Decision Tree, Random Forest, KNN, 
Extra Trees, Gradient Boosting). Random Forest achieved best validation performance (MAE: 0.0166, 
R²: 0.926) with strong test set generalization (MAE: 0.0212, R²: 0.889).

**Deployment**: Built Streamlit web app providing real-time delay predictions with risk classification 
and seasonal analysis. Live at [flightcast.streamlit.app](https://flightcast.streamlit.app/)
""")

st.markdown("**Key Findings**")

model_comparison = pd.DataFrame({
    'Model': ['Random Forest', 'Gradient Boosting', 'Ridge Regression', 'Decision Tree', 'Extra Trees', 'KNN'],
    'Validation MAE': [0.0166, 0.0185, 0.0231, 0.0320, 0.0353, 0.0649],
    'Validation R²': [0.9264, 0.9352, 0.7994, 0.8082, 0.7799, 0.1855]
})

st.dataframe(model_comparison, hide_index=True, use_container_width=True)

st.write("""
**Domain Insights**: June-July show worst delays (23.7% and 23.0% vs 19.3% baseline). September 
performs best (15.2%). Delta Airlines leads in reliability (14.4% delays) while Frontier shows 
worst performance (25.6% delays) - a 78% relative difference. 72% of delays stem from airline-controlled 
factors (carrier operations + late aircraft cascades) rather than external causes.

**Model Behavior**: Prediction accuracy degrades with operational scale (major hubs: 4.4pp error vs 
small airports: 0.9pp error). Model systematically underestimates extreme delays (predicts 38% for 
routes with actual 44% delays), indicating conservative bias in worst-case scenarios.
""")

st.markdown("---")

st.markdown("### Research Interests")

st.write("""
I'm interested in applying machine learning to mining operations, with potential focus areas including:

- Predictive maintenance for mining equipment using sensor data
- Ore grade prediction and resource estimation
- Production optimization and scheduling
- Safety risk prediction from operational indicators
- Equipment failure forecasting
- Blast optimization using historical performance data

My methodological interests include systematic model comparison, temporal validation strategies, 
feature engineering for operational data, and production deployment of predictive systems.
""")

st.markdown("---")

st.markdown("### Contact")

st.write("""
I am currently seeking postgraduate research opportunities in machine learning applications to mining. 
I'm particularly interested in programs or supervisors working on operational prediction problems 
in mining where rigorous model evaluation and practical deployment are priorities.

Email: smabuza782@gmail.com  
Location: Pietermaritzburg, South Africa
""")
