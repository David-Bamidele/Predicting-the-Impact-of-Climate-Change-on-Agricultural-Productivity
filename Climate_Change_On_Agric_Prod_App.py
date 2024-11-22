
# Import necessary libraries
import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model  
@st.cache_resource
def load_model():
    return joblib.load("Desktop/ClimateAgric.pkl")
model = load_model()

# Set up the Streamlit app
st.title('Predicting the Impact of Climate Change on Agricultural Productivity')
st.write("This app predicts the **Impact of Climate Change on Agricultural Productivity**.")


# Sidebar for user input
st.sidebar.header("Input Features")
st.sidebar.markdown("Adjust the sliders and inputs below to customize the prediction.")

# Input fields
year = st.sidebar.slider("Year", min_value=1990, max_value=2030, step=1, value=2024)
avg_temp = st.sidebar.number_input("Average Temperature (°C)", min_value=0.0, max_value=50.0, step=0.1)
precipitation = st.sidebar.number_input("Total Precipitation (mm)", min_value=0.0, max_value=5000.0, step=1.0)
co2_emissions = st.sidebar.number_input("CO2 Emissions (MT)", min_value=0.0, max_value=100.0, step=0.1)
pesticide_use = st.sidebar.number_input("Pesticide Use (KG/HA)", min_value=0.0, max_value=100.0, step=0.1)
fertilizer_use = st.sidebar.number_input("Fertilizer Use (KG/HA)", min_value=0.0, max_value=100.0, step=0.1)


# Create a dictionary for the model input
input_data = {
        "Year": year,
        "Average_Temperature_C": avg_temp,
        "Total_Precipitation_mm": precipitation,
        "CO2_Emissions_MT": co2_emissions,
        "Pesticide_Use_KG_per_HA": pesticide_use,
        "Fertilizer_Use_KG_per_HA": fertilizer_use,
   
                    }

# Convert the dictionary to a DataFrame
input_df = pd.DataFrame([input_data])

st.markdown("---")

# Display user input

# Display input data
st.subheader("User Input Summary")
st.dataframe(input_df, width=700)

st.markdown("---")

    # Load model and make prediction
prediction = model.predict(input_df)
    
    # Display prediction
if st.button("Predict Crop Yield"):
    # Make prediction when the button is clicked
    prediction = model.predict(input_df)

 # Display prediction
    st.subheader("Predicted Crop Yield (MT/HA)")
    st.write(f"{prediction[0]:,.2f}")

st.markdown("---")

st.caption("This App is developed to explore the intersection of **climate change** and **agricultural productivity** using machine learning.")

st.write("Contact Details")
st.caption("**Developer:** Bamidele David")  
st.caption("**Contact:** [davidbamidele16@gmail.com]")  
st.caption("**GitHub:** [https://github.com/David-Bamidele]")


