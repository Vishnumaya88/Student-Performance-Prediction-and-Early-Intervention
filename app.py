import streamlit as st
import pandas as pd
import pickle

# -------------------- CONFIG --------------------
st.set_page_config(page_title="Student Performance", layout="centered")

# -------------------- LOAD --------------------
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# -------------------- STYLE --------------------
st.markdown("""
<style>

/* ---------- GLOBAL TEXT ---------- */
html, body, [class*="css"]  {
    color: #E5E7EB;  /* light gray (visible in dark mode) */
}

/* ---------- TITLE ---------- */
.title {
    text-align: center;
    font-size: 34px;
    font-weight: 600;
    color: #F9FAFB;  /* strong white */
}
.subtitle {
    text-align: center;
    color: #9CA3AF;  /* readable gray */
    margin-bottom: 25px;
}

/* ---------- SECTION HEADERS ---------- */
.section {
    font-size: 18px;
    font-weight: 600;
    margin-top: 25px;
    margin-bottom: 10px;
    color: #F3F4F6;  /* brighter */
}

/* ---------- INPUT LABELS ---------- */
label {
    color: #E5E7EB !important;
    font-weight: 500;
}

/* ---------- BUTTON ---------- */
.stButton>button {
    background: linear-gradient(135deg, #2563EB, #1D4ED8);
    color: white;
    border-radius: 8px;
    height: 45px;
    font-size: 15px;
    border: none;
    font-weight: 500;
}
.stButton>button:hover {
    background: linear-gradient(135deg, #1D4ED8, #1E40AF);
}

/* ---------- RESULT BOX ---------- */
.result-pass {
    margin-top: 20px;
    padding: 14px;
    border-radius: 8px;
    background-color: #052e16;
    color: #bbf7d0;
    border: 1px solid #166534;
    text-align: center;
    font-weight: 600;
}

.result-fail {
    margin-top: 20px;
    padding: 14px;
    border-radius: 8px;
    background-color: #450a0a;
    color: #fecaca;
    border: 1px solid #7f1d1d;
    text-align: center;
    font-weight: 600;
}

/* ---------- SLIDER ---------- */
.stSlider > div > div {
    color: #3B82F6;
}

/* ---------- SELECTBOX TEXT ---------- */
div[data-baseweb="select"] {
    color: #E5E7EB;
}

/* ---------- GENERAL SPACING ---------- */
.block-container {
    padding-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------
st.markdown('<div class="title">Student Performance Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Machine Learning based academic prediction</div>', unsafe_allow_html=True)

# -------------------- ACADEMIC --------------------
st.markdown('<div class="section">Academic Details</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    studytime = st.selectbox("Study Time", [1, 2, 3, 4])
    G1 = st.slider("G1 (First Grade)", 0, 20)

with col2:
    failures = st.selectbox("Failures", [0, 1, 2, 3])
    G2 = st.slider("G2 (Second Grade)", 0, 20)

# -------------------- PERSONAL --------------------
st.markdown('<div class="section">Student Details</div>', unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    age = st.slider("Age", 15, 22)
    school = st.selectbox("School", ["GP", "MS"])

with col4:
    absences = st.slider("Absences", 0, 50)
    sex = st.selectbox("Sex", ["M", "F"])

# -------------------- DATA --------------------
input_data = pd.DataFrame({
    'age': [age],
    'studytime': [studytime],
    'failures': [failures],
    'absences': [absences],
    'school': [school],
    'sex': [sex],
    'G1': [G1],
    'G2': [G2]
})

input_data = pd.get_dummies(input_data)
input_data = input_data.reindex(columns=columns, fill_value=0)
input_scaled = scaler.transform(input_data)

# -------------------- PREDICT --------------------
st.write("")
if st.button("Predict", use_container_width=True):

    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.markdown('<div class="result-pass">Student is likely to PASS</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-fail">Student is likely to FAIL</div>', unsafe_allow_html=True)