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
I work on machine learning projects where the goal is to predict something real and explain the result clearly.
I like taking a big dataset, cleaning it properly, testing more than one model, and then building a simple app people can use.
Right now I am building toward postgraduate study in data and AI.
""")

st.divider()

st.subheader("Background")
st.write("""
I completed a Bachelor of Information and Communication Technology (BICT) at the University of Mpumalanga (2025).
In my final year I focused on Artificial Intelligence Applications (Machine Learning).
""")

st.divider()

st.subheader("Research interests (what I actually work on)")
st.write("""
- Prediction using real-world operational data (delays, performance, risk)
- Comparing models properly instead of using one model and guessing
- Understanding what affects the prediction (which features matter)
- Building a working demo so the work is easy to test and explain
""")

st.divider()

st.header("Featured work")

st.subheader("Flight Delay Predictor")
st.write("""
Goal: predict flight delay rates from historical flight data and test which model performs best.
I worked with a large dataset and reduced it to a clean dataset with over 130000 records for training and testing.
I removed the COVID period (2020 and 2021) to avoid unusual patterns that can distort the model.
""")

st.markdown("**How I approached it**")
st.write("""
1) Cleaned and prepared the dataset (missing values, filtering, basic feature prep)
2) Trained multiple models and compared results (ensemble learning approach)
3) Chose Random Forest as the final model because it performed best
4) Deployed the predictor as a simple Streamlit app
""")

st.markdown("**Models I tested**")
st.write("""
- Ridge Regression
- Decision Tree
- Random Forest (best)
- KNN
- Extra Trees
- Gradient Boosting
""")

st.markdown("**What made Random Forest the best for this**")
st.write("""
- It handled the feature patterns better than linear models
- It was strong on the test set compared to the other models I tried
- It gave stable performance instead of being too sensitive to small changes
""")

st.divider()

st.subheader("What I want to improve next (clear plan)")
st.write("""
For my next step, I want to move from “good prediction” to “useful insight”.
That means:

- Explain the prediction better (feature importance, what drives delays)
- Try better validation (time-based split instead of random split)
- Handle imbalance properly if most flights have low delay rates
- Add a stronger model comparison (tuning + cross validation)
- Expand the app so it shows confidence or uncertainty, not only a single number
""")
