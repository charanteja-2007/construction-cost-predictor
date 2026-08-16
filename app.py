import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.set_page_config(page_title="AI Construction Cost Predictor", layout="wide")

st.markdown("""
<style>
    .block-container {
        max-width: 900px;
        margin: 0 auto;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }

    h1 {
        font-size: 3rem !important;
        text-align: center;
    }

    p, label {
        font-size: 1.3rem !important;
    }

    /* Number input boxes */
    .stNumberInput input {
        font-size: 1.3rem !important;
        height: 3rem !important;
        border-radius: 10px !important;
    }

    /* Selectbox - target the visible text and container */
    div[data-baseweb="select"] {
        font-size: 1.3rem !important;
    }
    div[data-baseweb="select"] > div {
        min-height: 3.2rem !important;
        font-size: 1.3rem !important;
        display: flex !important;
        align-items: center !important;
        border-radius: 10px !important;
    }
    div[data-baseweb="select"] span {
        font-size: 1.3rem !important;
    }

    /* Predict button */
    .stButton {
        display: flex;
        justify-content: center;
    }
    .stButton button {
        font-size: 1.4rem !important;
        padding: 0.9rem 3rem !important;
        border-radius: 10px !important;
        width: 100%;
        max-width: 400px;
    }

    /* Result metrics */
    div[data-testid="stMetricValue"] {
        font-size: 2.2rem !important;
    }
    div[data-testid="stMetricLabel"] {
        font-size: 1.2rem !important;
    }

    /* Success/info boxes */
    .stAlert {
        font-size: 1.3rem !important;
        border-radius: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_models():
    cost_model = joblib.load('cost_model.pkl')
    cement_model = joblib.load('cement_model.pkl')
    steel_model = joblib.load('steel_model.pkl')
    le_structure = joblib.load('le_structure.pkl')
    le_location = joblib.load('le_location.pkl')
    le_grade = joblib.load('le_grade.pkl')
    return cost_model, cement_model, steel_model, le_structure, le_location, le_grade

cost_model, cement_model, steel_model, le_structure, le_location, le_grade = load_models()

st.title("AI Construction Cost & Material Predictor")
st.write("Enter your building specifications to estimate cost and material requirements.")

col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Built-up Area (sqft)", min_value=100, max_value=20000, value=1200)
    floors = st.number_input("Number of Floors", min_value=1, max_value=10, value=2)
    structure = st.selectbox("Structure Type", options=le_structure.classes_)

with col2:
    location = st.selectbox("Location Tier", options=le_location.classes_)
    grade = st.selectbox("Material Grade", options=le_grade.classes_)

st.write("")

if st.button("Predict Cost & Materials"):
    structure_enc = le_structure.transform([structure])[0]
    location_enc = le_location.transform([location])[0]
    grade_enc = le_grade.transform([grade])[0]

    input_data = pd.DataFrame([[area, floors, structure_enc, location_enc, grade_enc]],
                               columns=['area_sqft', 'floors', 'structure_type_enc',
                                        'location_tier_enc', 'material_grade_enc'])

    predicted_cost = cost_model.predict(input_data)[0]
    predicted_cement = cement_model.predict(input_data)[0]
    predicted_steel = steel_model.predict(input_data)[0]

    st.success(f" Estimated Total Cost: ₹{predicted_cost:,.0f}")

    c1, c2 = st.columns(2)
    with c1:
        st.metric("Cement Required", f"{predicted_cement:,.0f} bags")
    with c2:
        st.metric("Steel Required", f"{predicted_steel:,.0f} kg")

    st.caption(f"Cost per sqft: ₹{predicted_cost/area:,.0f}")

st.markdown("---")
st.caption("Model: Random Forest Regressor | Trained on synthetically generated construction cost data")