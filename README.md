#  Movie Revenue Prediction Web App

##  Project Overview

This project builds a Machine Learning model to predict movie revenue based on production and popularity features.  

The project demonstrates a complete end-to-end Data Science workflow including:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Selection
- Model Training & Evaluation
- Cross-Validation
- Model Deployment using Streamlit
- Version Control using Git & GitHub

---

##  Dataset Description

The dataset contains 100 movie records with features such as:

- Budget
- Runtime
- Vote Average
- Vote Count
- Release Year
- Genre
- Production Country

Target Variable:
> Revenue (Continuous — Regression Problem)

---

##  Model Used

### Linear Regression

Why Linear Regression?

- Strong linear correlation between Budget and Revenue (0.75)
- Small dataset (100 rows)
- Interpretable coefficients
- Outperformed Random Forest on this dataset

---

##  Model Performance

Test Set Results:

- R² Score: 0.50
- MAE: 124,698,725
- RMSE: 156,654,231

Cross-Validation (5-fold):

- Average R² Score: 0.43

The model explains approximately 43–50% of the revenue variance.

---

## Streamlit Web Application

The trained model is deployed using Streamlit.

Users can input:

- Budget
- Runtime
- Vote Average
- Vote Count
- Release Year

The app predicts estimated movie revenue.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Git & GitHub

---

