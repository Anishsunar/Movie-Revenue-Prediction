import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open('movie_revenue_model.pkl', 'rb'))

st.title("🎬 Movie Revenue Prediction App")

st.write("Enter movie details below:")

# User inputs
budget = st.number_input("Budget", min_value=0)
runtime = st.number_input("Runtime (minutes)", min_value=0)
vote_average = st.number_input("Vote Average", min_value=0.0)
vote_count = st.number_input("Vote Count", min_value=0)
release_year = st.number_input("Release Year", min_value=1900, max_value=2030)

if st.button("Predict Revenue"):
    input_data = np.array([[budget, runtime, vote_average, vote_count, release_year]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Revenue: ${prediction[0]:,.2f}")