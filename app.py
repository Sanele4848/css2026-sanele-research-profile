import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sanele Mabuza | Research Profile", layout="wide")

with st.sidebar:
    st.title("Sanele Mabuza")
    st.write("ML Practitioner")
    st.markdown("---")
    st.write("smabuza782@gmail.com")
    st.write("Pietermaritzburg, South Africa")
    st.write("[LinkedIn](https://www.linkedin.com/in/sanele-mabuza-a04742225/)")

st.title("Profile")

st.markdown("### About")

st.write("""
I work on machine learning applications with a focus on prediction problems. My undergraduate project involved flight delay prediction using ensemble methods, which developed my skills in model validation and deployment.

I'm interested in postgraduate study to apply machine learning techniques to the mining sector, where I see significant opportunities for predictive modeling in areas such as resource exploration and operational optimization.""")

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

st.markdown("### Final Year Project: Flight Delay Prediction")

st.write("""
My final year project predicted flight delay rates using U.S. airline data from 2013-2023. The dataset 
had 132,695 records covering 51.4 million flights across 21 airlines and 389 airports. I removed 
2020-2021 (COVID years) because those patterns weren't representative.
""")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Test MAE", "2.12 pp")
col2.metric("R² Score", "0.889")
col3.metric("Best Model", "Random Forest")
col4.metric("Features", "36 engineered")

st.markdown("**Methodology**")

st.write("""
**Data prep**: Removed COVID years. Split data by time (trained on 2013-2018, validated on 2019, 
tested on 2022-2023) instead of random split to avoid cheating. Log-transformed skewed variables 
and capped extreme outliers.

**Features**: Made 36 features including time patterns, historical averages, and operational stress 
indicators. The top 3 features did most of the work: past delay rate for that specific route and month 
(40% importance), number of flights (31%), and historical delay count (20%).

**Models**: Tested Ridge Regression, Decision Tree, Random Forest, KNN, Extra Trees, and Gradient Boosting. 
Random Forest won (validation MAE: 0.0166, R²: 0.926). On the test set it got MAE of 0.0212 and R² of 0.889.

**Deployment**: Built a Streamlit app that gives delay predictions. It's live at 
[flightcast.streamlit.app](https://flightcast.streamlit.app/)
""")

st.markdown("**Key Findings**")

model_comparison = pd.DataFrame({
    'Model': ['Random Forest', 'Gradient Boosting', 'Ridge Regression', 'Decision Tree', 'Extra Trees', 'KNN'],
    'Validation MAE': [0.0166, 0.0185, 0.0231, 0.0320, 0.0353, 0.0649],
    'Validation R²': [0.9264, 0.9352, 0.7994, 0.8082, 0.7799, 0.1855]
})

st.dataframe(model_comparison, hide_index=True, use_container_width=True)

st.write("""
June-July had the worst delays (23.7% and 23.0% vs baseline of 19.3%). September was best (15.2%). 
Delta was the most reliable airline (14.4% delays) and Frontier was worst (25.6%) - that's a 78% 
difference. 

72% of delays came from things airlines control (their own operations plus knock-on effects from 
earlier delays) rather than weather or external factors.

The model worked better on small airports (0.9pp error) than major hubs (4.4pp error). It also 
underestimated really bad delays - when actual delays were 44%, it predicted 38%.
""")

st.markdown("---")

st.markdown("### Interests")

st.write("""
I'm interested in ML for mining operations. Some areas I'm considering:

- Predicting equipment failures before they happen
- Estimating ore grades
- Optimizing production schedules
- Predicting safety risks
- Using blast data to improve future blasts

In terms of approach, I care about testing multiple models properly, using time-based validation 
when working with time series data, and building things that can actually be used.
""")


