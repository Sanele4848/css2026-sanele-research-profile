import streamlit as st

# --- PAGE SETTINGS ---
st.set_page_config(
    page_title="Sanele Mabuza | Graduate Profile",
    layout="wide"
)

# --- SIDEBAR ---
with st.sidebar:
    st.title("Sanele Mabuza")
    st.write("BICT Graduate (2025)")
    st.write("University of Mpumalanga")

    st.markdown("---")
    st.write("**Location:** South Africa")
    st.write("smabuza782@gmail.com")
    st.write("[LinkedIn Profile](https://www.linkedin.com/in/sanele-mabuza-a04742225/)")

# --- MAIN CONTENT ---
st.header("Profile")

st.write("""
I am a BICT graduate from the University of Mpumalanga. I enjoy working with data and building things that actually help people.
My main interest is machine learning and using it to solve real problems.

I am also preparing myself for postgraduate study, and I want to grow into a stronger researcher in data and AI.
Outside school, I have been learning deep learning on my own through online learning and practice projects.
""")

st.divider()

# --- EDUCATION ---
st.subheader("Education")
st.write("**Bachelor of Information and Communication Technology (BICT)**")
st.write("University of Mpumalanga | Completed: 2025")
st.write("Final year: Artificial Intelligence Applications (Machine Learning) - 81%")


st.write("""
I focused more on machine learning during my final year, and I am continuing to build my skills through projects and self-study.
""")

st.divider()

# --- PROJECTS ---
st.subheader("Key Academic Projects")

st.markdown("### Flight Delay Predictor")
st.write("**Project mark:** 84%")

st.write("""
I built a flight delay prediction project using a dataset with over 130000 records.
The goal was to predict flight delay rates and understand what drives delays.

I used ensemble learning and tested different models.
Random Forest gave the best results, so I used it as the final model.
""")

st.write("""
What I did:
* Cleaned the dataset and handled missing values
* Prepared features and did basic encoding
* Trained and compared multiple models
* Selected Random Forest as the final model
* Built a simple Streamlit app to test predictions
""")

st.divider()

# --- SKILLS ---
st.subheader("Technical Skills")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Core Skills**")
    st.write("* Python")
    st.write("* SQL and databases")
    st.write("* Data analysis (Pandas, NumPy)")
    st.write("* Machine learning (scikit-learn)")

with col2:
    st.markdown("**Extra Learning**")
    st.write("* Deep learning (self-study)")
    st.write("* Neural networks (practice)")

st.divider()

# --- CERTIFICATION ---
st.subheader("Certification")
st.write("I am currently preparing for:")
st.write("* Microsoft Certified: Azure Data Scientist Associate (DP-100)")

st.divider()

# --- INTERESTS ---
st.subheader("Postgraduate Interest")

st.write("""
For postgraduate work, I want to focus on real problems in South Africa.
I am interested in the mining sector and how data and AI can improve safety and daily operations.
""")
