# Student Performance Prediction and Early Intervention

## Problem Statement

The goal of this project is to predict whether a student will pass or fail based on demographic, academic, and behavioral factors. Early identification of at-risk students enables timely intervention and improves academic outcomes.

## Objectives

* Predict student performance (Pass/Fail)
* Identify at-risk students early
* Compare multiple machine learning models
* Explain predictions using LIME

## Dataset

This project uses the **UCI Student Performance Dataset**.

The dataset contains:

* Demographic information (age, gender, family background)
* Academic details (study time, failures, absences)
* Grades (G1, G2, G3)

Target Variable

Final grade (G3) is converted into:

* **Pass (1)** → G3 ≥ 10
* **Fail (0)** → G3 < 10

## Project Pipeline

1. Data Understanding

* Explored dataset structure and features
* Checked missing values and duplicates

2. Data Preprocessing

* Created target variable (Pass/Fail)
* Removed data leakage features (G1, G2, G3)
* Encoded categorical variables
* Performed train-test split
* Applied feature scaling

3. Exploratory Data Analysis (EDA)

* Pass vs Fail distribution
* Study time vs performance
* Absences vs performance
* Correlation heatmap

 4. Model Building

Three models were trained:
* Decision Tree Classifier
* Logistic Regression
* Gradient Boosting

Model Performance

| Model               | Accuracy         |
| ------------------- | ---------------- |
| Decision Tree       | 64.5%            |
| Logistic Regression | **70.9% (Best)** |
| Gradient Boosting   | 68.3%            |

Evaluation

* Logistic Regression performed best
* Model predicts passing students well
* Lower recall for failing students (important limitation)

Explainability (LIME)

LIME was used to explain individual predictions:

* Identifies key factors affecting predictions
* Highlights importance of:

  * Past failures
  * Study behavior
  * Social activity

Deployment

A Streamlit application is built to:
* Take user inputs (study time, absences, failures)
* Predict student performance (Pass/Fail)

Project Structure

```plaintext
student-performance-prediction/
│
├── data/
│   └── student-mat.csv
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_model_training.ipynb
│
├── app/
│   └── streamlit_app.py
│
├── model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
```

Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib, Seaborn
* LIME
* Streamlit

Key Insights

* Study time positively impacts performance
* Past failures strongly affect outcomes
* Absences negatively influence results
* Student performance depends on multiple factors

 Conclusion

Logistic Regression achieved the best performance and was selected as the final model. The integration of LIME provides transparency by explaining individual predictions, making the system useful for identifying at-risk students and enabling early intervention.


