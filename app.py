import streamlit as st
import pickle

from utils.predict import predict_top_diseases
from db.db_save import save_to_db

st.set_page_config(page_title="MediScope", layout="wide")

# Session state
if "page" not in st.session_state:
    st.session_state.page = 1

# ---------------- PAGE 1 ----------------
if st.session_state.page == 1:
    st.title("🩺 MediScope")

    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=1)
    gender = st.radio("Sex", ["Male", "Female"])

    if st.button("Continue"):
        if name:
            st.session_state.name = name
            st.session_state.age = age
            st.session_state.gender = gender
            st.session_state.page = 2

# ---------------- PAGE 2 ----------------
elif st.session_state.page == 2:
    st.title("Select Symptoms")

    symptoms_list = pickle.load(open("symptoms.pkl", "rb"))

    selected = st.multiselect("Search & Select Symptoms", symptoms_list)

    if st.button("Continue"):
        if selected:
            st.session_state.symptoms = selected
            st.session_state.page = 3

# ---------------- PAGE 3 ----------------
elif st.session_state.page == 3:
    st.title("Predicted Conditions")

    results = predict_top_diseases(st.session_state.symptoms)

    for disease, prob in results:
        percentage = round(prob * 100, 2)

        if percentage > 60:
            level = "Strong"
        elif percentage > 30:
            level = "Moderate"
        else:
            level = "Fair"

        st.write(f"### {disease}")
        st.progress(int(percentage))
        st.write(f"{level} match ({percentage}%)")
        st.write("---")

    # Save to DB
    save_to_db(
        st.session_state.name,
        st.session_state.age,
        st.session_state.gender,
        st.session_state.symptoms,
        results[0][0]
    )

    st.success("Data saved successfully!")