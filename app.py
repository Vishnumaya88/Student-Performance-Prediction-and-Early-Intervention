import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Student Predictor", page_icon="🎓", layout="centered")

# 🌈 Clean neutral styling (works in both modes)
st.markdown("""
<style>

/* Title */
h1 {
    text-align: center;
    font-weight: 600;
}

/* Subtitle */
.subtext {
    text-align: center;
    color: gray;
    margin-bottom: 30px;
}

/* Inputs spacing */
.stNumberInput, .stSelectbox {
    margin-bottom: 15px;
}

/* Button */
.stButton>button {
    width: 100%;
    height: 48px;
    border-radius: 12px;
    font-size: 16px;
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    color: white;
    border: none;
}

/* Result */
.result-pass {
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    font-weight: 500;
    margin-top: 20px;
    background-color: rgba(34,197,94,0.15);
    color: #16a34a;
}

.result-fail {
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    font-weight: 500;
    margin-top: 20px;
    background-color: rgba(239,68,68,0.15);
    color: #dc2626;
}

</style>
""", unsafe_allow_html=True)

# Title
st.title("🎓 Student Performance Prediction")
st.markdown('<div class="subtext">Early Risk Detection System</div>', unsafe_allow_html=True)

# Load model
model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# 👇 Clean input order (as you wanted)
age = st.number_input("🎂 Age", 15, 25, 18)
studytime = st.selectbox("📚 Study Time", [1,2,3,4])
absences = st.number_input("📉 Absences", 0, 100, 5)
failures = st.selectbox("❌ Failures", [0,1,2,3])

# Prepare input
input_data = {
    'age': age,
    'studytime': studytime,
    'absences': absences,
    'failures': failures
}

# Fill missing columns
for col in columns:
    if col not in input_data:
        input_data[col] = 0

input_df = pd.DataFrame([input_data])[columns]

# Predict
if st.button("🚀 Predict Performance"):
    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.markdown(
            '<div class="result-pass">✅ Student is likely to PASS</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="result-fail">⚠️ Student is at risk of FAILING</div>',
            unsafe_allow_html=True
        )