import streamlit as st
import requests
import pandas as pd

API_URL = "http://api:8000"

st.set_page_config(
    page_title="Calorie Burnt Predictor",
    page_icon="🔥",
    layout="wide"
)

st.title("🔥 Calorie Burnt Predictor System")

st.markdown(
    "Predict calories burned during exercise using Machine Learning."
)

st.subheader("Enter Exercise Details")

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["male", "female"]
    )

    age = st.number_input(
        "Age",
        min_value=10,
        max_value=100,
        value=25
    )

    height = st.number_input(
        "Height (cm)",
        min_value=100.0,
        max_value=250.0,
        value=175.0
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=20.0,
        max_value=250.0,
        value=70.0
    )

with col2:

    duration = st.number_input(
        "Duration (minutes)",
        min_value=1.0,
        max_value=300.0,
        value=30.0
    )

    heart_rate = st.number_input(
        "Heart Rate",
        min_value=50.0,
        max_value=220.0,
        value=120.0
    )

    body_temp = st.number_input(
        "Body Temperature",
        min_value=35.0,
        max_value=45.0,
        value=38.5
    )

if st.button("Predict Calories Burned"):

    payload = {
        "Gender": gender,
        "Age": age,
        "Height": height,
        "Weight": weight,
        "Duration": duration,
        "Heart_Rate": heart_rate,
        "Body_Temp": body_temp
    }

    try:

        response = requests.post(
            f"{API_URL}/predict",
            json=payload
        )

        result = response.json()

        st.success(
            f"Predicted Calories Burned: "
            f"{result['predicted_calories']}"
        )

    except Exception as e:

        st.error(
            f"Error: {e}"
        )

st.divider()

st.subheader("Prediction History")

if st.button("Load Prediction History"):

    try:

        response = requests.get(
            f"{API_URL}/predictions"
        )

        data = response.json()

        if len(data) > 0:

            df = pd.DataFrame(data)

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.info(
                "No predictions found."
            )

    except Exception as e:

        st.error(
            f"Error: {e}"
        )