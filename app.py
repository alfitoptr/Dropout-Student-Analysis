import streamlit as st
import pandas as pd
import joblib

@st.cache_resource
def load_model():
    model = joblib.load("model/model.pkl")
    scaler = joblib.load("model/scaler.pkl")
    return model, scaler    
    
@st.cache_data  
def load_features():    
    with open("columns.txt", "r") as file:  
        features = [line.strip() for line in file.readlines()]
    return features 

model, scaler = load_model()

st.markdown(
    """
    <style>
        .block-container { padding: 2rem; }
        .stButton>button { width: 100%; }
    </style>
    """, 
    unsafe_allow_html=True
)

st.title("🎓 Student Status Prediction")

features = load_features()

user_input = {}

with st.expander("🔍 Masukkan Data"):
    num_cols = min(len(features), 6)  
    columns = st.columns(num_cols)

    for i, feature in enumerate(features):
        col = columns[i % num_cols]  
        user_input[feature] = col.number_input(feature, value=0)

if st.button("🔮 Prediction"):
    input_df = pd.DataFrame([user_input])
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]

    st.subheader("📢 Prediction result:")
    if prediction == 1:
        st.error("⚠️ **Students are likely to Dropout!**")
    else:
        st.success("✅ **Students are unlikely to drop out**")